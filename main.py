from fastapi import FastAPI
from Segments.BaseModel import PatientData
from ADT.A04 import json_to_hl7_a04
from ACK.ACK import create_ack
import requests
import traceback

app = FastAPI()

# Mapping of triggers to generator functions
ADT_TRIGGER_MAPPING = {
    "A04": json_to_hl7_a04,
    "A08": json_to_hl7_a08
}


@app.post("/send_hl7/")
async def send_hl7(patient: PatientData):
    data = patient.dict()

    # Step 1: Validate trigger
    trigger_event = data.get("trigger_event")
    if not trigger_event:
        return {"error": "Missing 'trigger_event' in request data."}

    # Step 2: Convert JSON -> HL7
    try:
        hl7_generator = ADT_TRIGGER_MAPPING.get(trigger_event.upper())
        if not hl7_generator:
            return {"error": f"Unsupported trigger: {trigger_event}"}

        hl7_message = hl7_generator(data)

        # Ensure HL7 message is a string (FastAPI-safe)
        if hasattr(hl7_message, "to_er7"):
            hl7_message = hl7_message.to_er7()
        elif not isinstance(hl7_message, str):
            hl7_message = str(hl7_message)

    except Exception as e:
        error_details = traceback.format_exc()
        print("⚠️ HL7 Conversion Exception:\n", error_details)
        return {"error": f"HL7 conversion failed: {str(e)}"}

    # Step 3: Send HL7 to NABIDH endpoint
    try:
        hl7_endpoint = "https://developerstg.dha.gov.ae/api/nabidhtesting/hl7testutility?app_id=a830a5be&app_key=10ea058592008b19969f3116832962b8"  # replace with actual endpoint
        headers = {"Content-Type": "text/plain"}
        response = requests.post(hl7_endpoint, data=hl7_message, headers=headers)

        # Capture NABIDH response text safely
        validation_response = response.text

    except Exception as e:
        return {"error": f"Failed to send HL7 to NABIDH: {str(e)}"}

    # Step 4: Generate ACK (always a string)
    try:
        ack_message = create_ack(data, validation_response)
        if hasattr(ack_message, "to_er7"):
            ack_message = ack_message.to_er7()
        elif not isinstance(ack_message, str):
            ack_message = str(ack_message)
    except Exception as e:
        ack_message = f"ACK generation failed: {str(e)}"

    # Step 5: Return everything safely
    return {
        "Trigger Event": trigger_event,
        "HL7 Message Sent": hl7_message,
        "NABIDH Validation Response": validation_response,
        "ACK Response": ack_message,
    }

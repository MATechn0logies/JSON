from fastapi import FastAPI
from Segments.BaseModel import PatientData
from Segments import BaseModel
from ADT.A03 import json_to_hl7_a03
from ADT.A04 import json_to_hl7_a04
from ADT.A08 import json_to_hl7_a08
from ADT.A11 import json_to_hl7_a11
from ADT.A13 import json_to_hl7_a13
from ADT.A28 import json_to_hl7_a28
from ADT.A31 import json_to_hl7_a31
from ADT.A39 import json_to_hl7_a39
from ADT.A40 import json_to_hl7_a40
from ORU.R01 import json_to_hl7_oru
from PPR.PRP import json_to_hl7_ppr_pc1
from MDM.MDMT02 import json_to_hl7_MDM
from ORM.O01 import json_to_hl7_ORM_O01
from OMP.OMPO09 import json_to_hl7_OMP_O09
from VXU.VXUV04 import json_to_hl7_vxu


import Segments.BaseModel
from ACK.ACK import create_ack
import requests
import traceback

app = FastAPI()

# Mapping of triggers to generator functions
TRIGGER_MAPPING = {
    "A03": json_to_hl7_a03,
    "A04": json_to_hl7_a04,
    "A08": json_to_hl7_a08,
    "A11": json_to_hl7_a11,
    "A13": json_to_hl7_a13,
    "A28": json_to_hl7_a28,
    "A31": json_to_hl7_a31,
    "A39": json_to_hl7_a39,
    "A40": json_to_hl7_a40,
    "R01" : json_to_hl7_oru,
    "T02" : json_to_hl7_MDM,
    "T08" : json_to_hl7_MDM,
    "O01" : json_to_hl7_ORM_O01,
    "O09" : json_to_hl7_OMP_O09,
    "V04" : json_to_hl7_vxu,
    "PC1": json_to_hl7_ppr_pc1,

    
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
        hl7_generator = TRIGGER_MAPPING.get(trigger_event.upper())
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

from pydantic import BaseModel
from hl7apy.core import Message
from datetime import datetime
import uuid


def create_ack(data: dict, validation_response: str) -> str:
    # --- Create base ACK message ---
    ack = Message("ACK", version="2.5")

    # --- MSH Segment ---
    ack.MSH.MSH_1 = "|"
    ack.MSH.MSH_2 = "^~\\&"
    ack.MSH.MSH_3 = "NABIDH"  
    ack.MSH.MSH_4 = "DHA"
    ack.MSH.MSH_5 = data.get("source_app") or "EMRSystem"
    ack.MSH.MSH_6 = data.get("facility_id_NABIDH") or "UnknownFacility"
    ack.MSH.MSH_7 = datetime.now().strftime("%Y%m%d%H%M%S")
    ack.MSH.MSH_9 = "ACK"
    ack.MSH.MSH_10 = str(uuid.uuid4().hex[:12]) 
    ack.MSH.MSH_11 = "T"  
    ack.MSH.MSH_12 = "2.5"
    ack.MSH.MSH_18 = "UTF-8"

    # --- MSA Segment ---
    ack.add_segment("MSA")

    # Determine acknowledgment code
    ack_code = "AA" if "Success" in validation_response else "AE"

    ack.MSA.MSA_1 = ack_code
    ack.MSA.MSA_2 = data.get("message_control_id") or "UNKNOWN"
    ack.MSA.MSA_3 = (
        "Message Accepted successfully."
        if ack_code == "AA"
        else f"Error: {validation_response}"
    )

    return ack.to_er7()

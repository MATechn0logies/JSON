from hl7apy.core import Segment
from datetime import datetime
import uuid

def json_to_hl7_MSH(data: dict) -> str:
    """
    Generate a generic MSH (Message Header) segment usable for ADT, ORU, VXU, etc.
    """

    msh = Segment("MSH", version="2.5")

    # HL7 Standard Field Separators
    msh.MSH_1 = "|"             # Field Separator
    msh.MSH_2 = "^~\\&"         # Encoding Characters

    # Sending and Receiving Information
    msh.MSH_3 = data.get("source_app", "EMRSystem")                 # Sending Application
    msh.MSH_4 = data.get("sending_facility") or data.get("facility_id_NABIDH", "TESTFACILITY")  # Sending Facility
    msh.MSH_5 = data.get("receiving_app", "NABIDH")                 # Receiving Application
    msh.MSH_6 = data.get("receiving_facility", "DHA")               # Receiving Facility

    # Date/Time of Message
    msh.MSH_7 = data.get("message_datetime", datetime.now().strftime("%Y%m%d%H%M%S"))

    # Message Type (e.g., ADT^A04, ORU^R01, VXU^V04)
    event_type = (
        data.get("event")                # Full event, e.g. "ADT^A04"
        or data.get("event_type")        # Alternate field name
        or data.get("trigger_event")     # Simplified (e.g. "A04", "ORU")
    )

    if event_type:
        # Automatically build ADT^A04-style message type if only trigger given
        if "^" not in event_type:
            # Guess message type prefix based on trigger
            if event_type.startswith("A"):
                event_type = f"ADT^{event_type}"
            elif event_type.startswith("R"):
                event_type = f"ORU^{event_type}"
            elif event_type.startswith("V"):
                event_type = f"VXU^{event_type}"
            elif event_type.startswith("T"):
                event_type = f"MDM^{event_type}"
            elif event_type.startswith("O01"):
                event_type = f"ORM^{event_type}"
            elif event_type.startswith("O09"):
                event_type = f"OMP^{event_type}"
            elif event_type.startswith("PC1"):
                event_type = f"PPR^{event_type}"
            else:
                event_type = f"HL7^{event_type}"
        msh.MSH_9 = event_type
    else:
        msh.MSH_9 = "ADT^A01"  # Fallback default

    # Message Control ID (unique ID per message)
    msh.MSH_10 = data.get("message_control_id", uuid.uuid4().hex)

    # Processing ID (T = Test, P = Production)
    msh.MSH_11 = data.get("processing_id", "T")

    # Version ID
    msh.MSH_12 = data.get("version_id", "2.5")

    # Character Set (default UTF-8)
    msh.MSH_18 = data.get("character_set", "UTF-8")

    return msh.to_er7()

from Segments.MSH import json_to_hl7_MSH
from Segments.EVN import json_to_hl7_EVN
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1

def json_to_hl7_a11(data: dict) -> str:
    """
    Convert JSON patient data into a complete HL7 ADT^A04 message.
    (Patient registration / admission message)
    """

    # ---- Generate Core Segments ----
    msh = json_to_hl7_MSH(data)
    evn = json_to_hl7_EVN(data)
    pid = json_to_hl7_PID(data)
    pv1 = json_to_hl7_PV1(data)

    # ---- Optional Segments ----
    optional_segments = []

    # PD1: Patient Additional Demographic (optional)

    hl7_message = "\r".join(
        segment for segment in [msh, evn, pid, pv1, *optional_segments] if segment
    )

    return hl7_message

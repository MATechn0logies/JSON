from Segments.MSH import json_to_hl7_MSH
from Segments.EVN import json_to_hl7_EVN
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.OBX import json_to_hl7_OBX  


def json_to_hl7_a08(data: dict) -> str:
    """
    Convert JSON patient data into a complete HL7 ADT^A08 message.
    PV1 and OBX segments are optional — included only if data exists.
    """

    # ---- Required Segments ----
    msh = json_to_hl7_MSH(data)
    evn = json_to_hl7_EVN(data)
    pid = json_to_hl7_PID(data)

    # ---- Optional Segments ----
    hl7_segments = [msh, evn, pid]

    # PV1 (optional)
    if data.get("patient_class"):
        hl7_segments.append(json_to_hl7_PV1(data))

    # OBX (optional, can have multiple)
    if data.get("OBX"):
        for obx_item in data["OBX"]:
            hl7_segments.append(json_to_hl7_OBX(obx_item))

    # ---- Final HL7 Message ----
    hl7_message = "\r".join(segment for segment in hl7_segments if segment)
    return hl7_message

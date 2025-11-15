from Segments.MSH import json_to_hl7_MSH
from Segments.EVN import json_to_hl7_EVN
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.OBX import json_to_hl7_OBX  
from Segments.AL1 import json_to_hl7_AL1
from Segments.DG1 import json_to_hl7_DG1
from Segments.PR1 import json_to_hl7_PR1
from Segments.IN1 import json_to_hl7_IN1


def json_to_hl7_a08(data: dict) -> str:

    # ---- Required Segments ----
    msh = json_to_hl7_MSH(data)
    evn = json_to_hl7_EVN(data)
    pid = json_to_hl7_PID(data)

    # ---- Optional Segments ----
    hl7_segments = [msh, evn, pid]

    
    if data.get("patient_class"):
        hl7_segments.append(json_to_hl7_PV1(data))

    
    if data.get("OBX"):
        for obx_item in data["OBX"]:
            hl7_segments.append(json_to_hl7_OBX(obx_item))


    if data.get("AL1"):
        for AL1_item in data["AL1"]:
            hl7_segments.append(json_to_hl7_AL1(AL1_item))


    if data.get("DG1"):
        for DG1_item in data["DG1"]:
            hl7_segments.append(json_to_hl7_DG1(DG1_item))


    
    if data.get("PR1"):
        for pr1_item in data["PR1"]:
            hl7_segments.append(json_to_hl7_PR1(pr1_item))

    if data.get("IN1"):
        for IN1_item in data["IN1"]:
            hl7_segments.append(json_to_hl7_IN1(IN1_item))


    # ---- Final HL7 Message ----
    hl7_message = "\r".join(segment for segment in hl7_segments if segment)
    return hl7_message

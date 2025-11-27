from  Segments.MSH import json_to_hl7_MSH
from  Segments.PID import json_to_hl7_PID
from  Segments.PV1 import json_to_hl7_PV1
from Segments.IN1 import json_to_hl7_IN1
from  Segments.ORC import json_to_hl7_ORC   
from Segments.RXA import json_to_hl7_RXA
from Segments.OBX import json_to_hl7_OBX
from Segments.NTE import json_to_hl7_NTE

def json_to_hl7_vxu(data: dict) -> str:
    VXU_segments = []


    # MSH Segment
    VXU_segments.append(json_to_hl7_MSH(data))  
    # PID Segment
    VXU_segments.append(json_to_hl7_PID(data))
    # PV1 Segment
    VXU_segments.append(json_to_hl7_PV1(data))
    # IN1 Segment (Optional)
    if data.get("IN1"):
        VXU_segments.append(json_to_hl7_IN1(data["IN1"]))
    # ORC Segment
    if not data.get("ORC"):
        raise Exception("❌ ORC segment is required for VXU message")
    VXU_segments.append(json_to_hl7_ORC(data["ORC"]))
    # RXA Segment
    if not data.get("RXA"):
        raise Exception("❌ RXA segment is required for VXU message")
    VXU_segments.append(json_to_hl7_RXA(data["RXA"]))
    # OBX Segments (Optional, can have multiple)
    if data.get("OBX"):
        for obx_item in data["OBX"]:
            VXU_segments.append(json_to_hl7_OBX(obx_item))

    if data.get("NTE"):
        for nte_item in data["NTE"]:
            nte_segment = json_to_hl7_NTE(nte_item)
            VXU_segments.append(nte_segment)
            
    return "\r".join(VXU_segments)
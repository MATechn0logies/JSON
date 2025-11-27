from hl7apy.core import Segment
from Segments.MSH import json_to_hl7_MSH
from Segments.EVN import json_to_hl7_EVN
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.TXA import json_to_hl7_TXA
from Segments.MDMOBX import json_to_hl7_OBX
from Segments.NTE import json_to_hl7_NTE

def json_to_hl7_MDM(data: dict) -> str:
    msh = json_to_hl7_MSH(data)
    evn = json_to_hl7_EVN(data)
    pid = json_to_hl7_PID(data)
    pv1 = json_to_hl7_PV1(data)

    # TXA for document header
    txa = json_to_hl7_TXA(data["TXA"])

    # OBX for document content (base64)
    obx_segments = []
    for obx_item in data.get("OBX", []):
        obx_segments.append(json_to_hl7_OBX(obx_item))

    segments = [msh, evn,pid, pv1, txa] + obx_segments

    if data.get("NTE"):
        for nte_item in data["NTE"]:
            nte_segment = json_to_hl7_NTE(nte_item)
            segments.append(nte_segment)

    return "\r".join(segments)

from Segments.MSH import json_to_hl7_MSH
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.ORC import json_to_hl7_ORC
from Segments.OBR import json_to_hl7_OBR
from Segments.NTE import json_to_hl7_NTE

def json_to_hl7_oru(data: dict) -> str:

    msh = json_to_hl7_MSH(data)
    pid = json_to_hl7_PID(data)
    pv1 = json_to_hl7_PV1(data)


    if not data.get("ORC"):
        raise Exception("❌ ORC required for ORU order")
    if not data.get("OBR"):
        raise Exception("❌ OBR required for ORU order")

    orc = json_to_hl7_ORC(data["ORC"])
    obr = json_to_hl7_OBR(data["OBR"])

    if data.get("NTE"):
        NTE = json_to_hl7_NTE(data["NTE"])
        segments = [msh, pid, pv1, orc, obr, NTE]
    else:
        segments = [msh, pid, pv1, orc, obr]


  

    return "\r".join(segments)

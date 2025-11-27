from Segments.MSH import json_to_hl7_MSH
from Segments.EVN import json_to_hl7_EVN
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1


def json_to_hl7_a03(data: dict) -> str:
  

    msh = json_to_hl7_MSH(data)
    evn = json_to_hl7_EVN(data)
    pid = json_to_hl7_PID(data)
    pv1 = json_to_hl7_PV1(data)

    segments =[msh,evn,pid,pv1]

    # ---- Optional Segments ----



    if data.get("AL1"):
        for AL1_item in data["AL1"]:
            AL1 = json_to_hl7_AL1(AL1_item)
            segments.append(AL1)



    

    return "\r".join(segments)

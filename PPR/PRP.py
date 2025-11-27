from Segments.MSH import json_to_hl7_MSH
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.PRB import json_to_hl7_PRB
from Segments.NTE import json_to_hl7_NTE  

def json_to_hl7_ppr_pc1(data: dict) -> str:
    """
    Build PPR^PC1 HL7 message (Problems Record)
    PV1 optional
    PRB required (can repeat)
    NTE optional under each PRB
    """

    segments = []

    # MSH & PID required
    segments.append(json_to_hl7_MSH(data))
    segments.append(json_to_hl7_PID(data))
    segments.append(json_to_hl7_PV1(data))
     # Empty separator for PV1



    # ---- PV1 optional ----
    

    # ---- PRB required ----
    if not data.get("PRB"):
        raise ValueError("PRB segment required in PPR message")

    for prb_item in data["PRB"]:
        segments.append(json_to_hl7_PRB(prb_item))

        # ---- NTE under each PRB ----
        if prb_item.get("NTE"):
            for nte_item in prb_item["NTE"]:
                segments.append(json_to_hl7_NTE(nte_item))

    return "\r".join(segments)

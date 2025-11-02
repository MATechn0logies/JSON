from Segments.MSH import json_to_hl7_MSH
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.PRB import json_to_hl7_PRB
from Segments.NTE import json_to_hl7_NTE  # must exist same style

def json_to_hl7_ppr_pc1(data: dict) -> str:
    """
    Build PPR^PC1 HL7 message (Problems Record)
    PV1 optional
    PRB required (can repeat)
    NTE optional under each PRB
    """

    # Core segments
    msh = json_to_hl7_MSH(data)
    pid = json_to_hl7_PID(data)

    segments = [msh, pid]

    # ---- PV1 optional ----
    if data.get("patient_class"):
        segments.append(json_to_hl7_PV1(data))

    # ---- PRB required ----
    if not data.get("PRB"):
        raise ValueError("PRB segment required in PPR message")

    for prb in data["PRB"]:
        segments.append(json_to_hl7_PRB(prb))

        # ---- NTE optional under PRB ----
        if prb.get("NTE"):
            for nte in prb["NTE"]:
                segments.append(json_to_hl7_NTE(nte))

    return "\r".join(s for s in segments if s)

from Segments.MSH import json_to_hl7_MSH
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.PRB import json_to_hl7_PRB
from Segments.NTE import json_to_hl7_NTE

def json_to_hl7_ppr_pc1(data: dict) -> str:

    segments = []

    # REQUIRED
    segments.append(json_to_hl7_MSH(data))
    segments.append(json_to_hl7_PID(data))

    # OPTIONAL PV1
    if data.get("PV1"):
        segments.append(json_to_hl7_PV1(data["PV1"]))

    # REQUIRED PRB (multiple allowed)
    prb_list = data.get("PRB")
    if not prb_list:
        raise ValueError("PRB is required for PPR-PC1 Message")

    for prb in prb_list:
        segments.append(json_to_hl7_PRB(prb))

        # OPTIONAL NTE below PRB
        if "NTE" in prb and prb["NTE"]:
            for nte in prb["NTE"]:
                segments.append(json_to_hl7_NTE(nte))

    return "\r".join(segments)

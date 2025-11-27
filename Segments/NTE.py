from hl7apy.core import Segment

def json_to_hl7_NTE(data: dict) -> str:
    nte = Segment("NTE", version="2.5")
    nte.NTE_1 = data.get("set_id", "")
    nte.NTE_3 = data.get("comment", "")
    return nte.to_er7()

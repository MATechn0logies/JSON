from hl7apy.core import Segment

def json_to_hl7_MRG(data: dict) -> str:
    mrg = Segment("MRG", version="2.5")

    mrg.MRG_1 = data.get("MRG1", "")
    mrg.MRG_5 = data.get("MRG5", "")

    return mrg.to_er7()

from hl7apy.core import Segment

def json_to_hl7_MRG(data: dict) -> str:
    mrg = Segment("MRG", version="2.5")

    # Correctly map JSON keys to MRG fields
    mrg.MRG_1 = data.get("prior_patient_id", "")
    mrg.MRG_5 = data.get("prior_visit_number", "")

    

    return mrg.to_er7()

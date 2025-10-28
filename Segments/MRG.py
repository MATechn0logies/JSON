from hl7apy.core import Segment

def json_to_hl7_MRG(data: dict) -> str:
    

    mrg = Segment("MRG", version="2.5")

    # 1. Prior Patient Identifier List (victim/source MRN)
    # Format: <MRN>^^^<FacilityName>^MRN
    mrg.MRG_1 = f"{data.get('prior_patient_id', '')}^^^{data.get('facility_name', '')}^MRN"

    # 5. Prior Visit Number (encounter to merge)
    mrg.MRG_5 = data.get("prior_visit_number", "")


    return mrg.to_er7()

from hl7apy.core import Segment

def json_to_hl7_AL1(data: dict) -> str:

    # NABIDH allows "AL1|\"\"\"\"" to clear all previous allergies
    if data.get("delete_all") == True:
        return 'AL1|""""'

    al1 = Segment("AL1", version="2.5")

    # --- Required Fields ---
    al1.AL1_1 = data.get("set_id")                                 # Set ID
    al1.AL1_2 = data.get("allergen_type_code")                     # e.g. FA^Food allergy^NAB042
    al1.AL1_3 = data.get("allergen_code")                          # e.g. 91930004^EGG DERIVED^NAB043
    al1.AL1_4 = data.get("allergy_severity_code")                  # e.g. SV^Severe^HL7128
    al1.AL1_5 = data.get("allergy_reaction")                       # e.g. Hives
    al1.AL1_6 = data.get("identification_date")                    # e.g. 20200906

    return al1.to_er7()

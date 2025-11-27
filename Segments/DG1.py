from hl7apy.core import Segment

def json_to_hl7_DG1(data: dict) -> str:
    """
    Convert JSON to DG1 (Diagnosis) Segment - NABIDH simplified structure.
    Only includes required and used fields per NABIDH 4.10 specification.
    """
    dg1 = Segment("DG1", version="2.5")

    dg1.DG1_1 = data.get("set_id")                                  # Set ID
    dg1.DG1_2 = data.get("diagnosis_coding_method", "I10")          # Diagnosis coding method (I10/SCT)
    dg1.DG1_3 = data.get("diagnosis_code")                          # Diagnosis code (Code^Description^System)
    dg1.DG1_4 = data.get("diagnosis_description")                   # Diagnosis description (text)
    dg1.DG1_5 = data.get("diagnosis_datetime")                      # Diagnosis date/time
    dg1.DG1_6 = data.get("diagnosis_type", "F")                     # Diagnosis type (A, W, F, O, P — usually F = Final)
    dg1.DG1_15 = data.get("diagnosis_priority", "1")                # Diagnosis priority (1 = Primary)
    dg1.DG1_16 = data.get("diagnosing_clinician")                   # Diagnosing clinician (Sheryan ID format)
    dg1.DG1_21 = data.get("diagnosis_action_code", "A")             # Action Code (A=Add, D=Delete, U=Update)

    return dg1.to_er7()

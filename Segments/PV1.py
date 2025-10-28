from hl7apy.core import Segment

def json_to_hl7_PV1(data: dict) -> str:
    """
    Generate PV1 (Patient Visit) segment from JSON data.
    Works for ADT, ORU, VXU, etc.
    """

    pv1 = Segment("PV1", version="2.5")

    # PV1-1: Set ID - PV1
    pv1.PV1_1 = "1"

    # PV1-2: Patient Class (I = Inpatient, O = Outpatient, E = Emergency)
    pv1.PV1_2 = data.get("patient_class", "O")

    # PV1-3: Assigned Patient Location
    # Format: Point of Care ^ Room ^ Bed ^ Facility
    pv1.PV1_3 = data.get("location") or "^^^DEFAULTFACILITY"
    pv1.pv1_4 = data.get("admission_type", "O")  # PV1-4: Admission Type
    # PV1-7: Attending Doctor
    pv1.PV1_7 = data.get("attending_doctor")

    # PV1-8: Referring Doctor
    pv1.PV1_8 = data.get("referring_doctor")

    # PV1-9: Consulting Doctor (optional)
    if data.get("consulting_doctor"):
        pv1.PV1_9 = data.get("consulting_doctor")

    # PV1-10: Hospital Service (optional, default "ALG")
    pv1.PV1_10 = data.get("hospital_service", "ALG")

    # PV1-14: Admit Source (optional)
    pv1.PV1_14 = data.get("admit_source", "2")

    # PV1-18: Patient Type (optional)
    pv1.PV1_18 = data.get("patient_type", "R")

    # PV1-19: Visit Number
    pv1.PV1_19 = data.get("visit_number") or "1"

  

    # PV1-44: Admit Date/Time
    pv1.PV1_44 = data.get("admit_datetime")

    if data.get("trigger_event") == "A03":
        # PV1-36: Discharge Disposition (optional)
        if data.get("discharge_disposition"):
            pv1.PV1_36 = data["discharge_disposition"]

        # PV1-45: Discharge Date/Time (required for A03)
        if not data.get("discharge_datetime"):
            raise ValueError("❌ Missing required PV1-45 (discharge_datetime) for ADT^A03 message")
        else:
            pv1.PV1_45 = data["discharge_datetime"]

    # PV1-50: Alternate Visit ID (optional)
    if data.get("alternate_visit_id"):
        pv1.PV1_50 = data["alternate_visit_id"]

    return pv1.to_er7()

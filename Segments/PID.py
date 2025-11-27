from hl7apy.core import Segment

def json_to_hl7_PID(data: dict) -> str:
    """
    Generate PID segment from JSON data.
    Works for ADT, ORU, VXU, etc.
    """

    pid = Segment("PID", version="2.5")

    # PID-1: Set ID
    pid.PID_1 = "1"

    # PID-3: Patient Identifier List — includes MRN and Government ID
    pid.PID_3[0] =  f"{data.get('patient_id')}^^^{data.get('facility_id_NABIDH')}^MRN"  # MRN (local)
    pid.PID_3[1] =    f"{data.get('government_id')}^^^GOVERNMENT^PPN"   

    # PID-5: Patient Name (Lastname^Firstname^Middlename^^^^Title)
    pid.PID_5 = data.get("patient_name")

    # PID-7: Date/Time of Birth
    pid.PID_7 = data.get("dob")

    # PID-8: Administrative Sex
    pid.PID_8 = data.get("gender")

    # PID-10: Race
    pid.PID_10 = data.get("race")

    # PID-11: Patient Address (street^^city^state^zip^country^address_type)
    pid.PID_11 = data.get("address")

    # PID-13: Phone Number (Home)
    if data.get("phone"):
        pid.PID_13 = f"{data['phone']}^PRN^PH"

    # PID-14: Phone Business (if available)
    if data.get("phone_business"):
        pid.PID_14 = f"{data['phone_business']}^WPN^PH"

    # PID-15: Primary Language
    pid.PID_15 = data.get("language")

    # PID-16: Marital Status
    pid.PID_16 = data.get("marital_status")

    # PID-17: Religion
    pid.PID_17 = data.get("religion")

    # PID-19: National ID (Emirates ID)
    pid.PID_19 = data.get("emirates_id")

    # PID-22: Ethnic Group (defaults to Unknown if not provided)
    pid.PID_22 = data.get("ethnic_group") or "UNK^Unknown^NAB005"

    # PID-28: Nationality
    pid.PID_28 = data.get("nationality")

    pid.PID_30 = data.get("Death_indicator", "N")                            # Birth Place

    # PID-30: Patient Death Indicator (optional)
    pid.PID_31 = "O"                                          # Identity Unknown Indicator

    # PID-33: Last Update Date/Time
    pid.PID_33 = data.get("record_datetime") or data.get("message_datetime")

    return pid.to_er7()

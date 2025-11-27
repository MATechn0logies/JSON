from hl7apy.core import Segment

def json_to_hl7_IN1(data: dict) -> str:
    IN1= Segment("IN1", version="2.5")

    IN1.IN1_1 = data.get("set_id")
    IN1.IN1_2 = data.get("insurance_plan_id")
    IN1.IN1_3 = data.get("insurance_company_id")
    IN1.IN1_4 = data.get("insurance_company_name")
    IN1.IN1_5 = data.get("insurance_company_address")
    IN1.IN1_6 = data.get("insurance_co_contact_person")
    IN1.IN1_7 = data.get("insurance_co_phone_number")
    IN1.IN1_8 = data.get("group_number")
    IN1.IN1_9 = data.get("group_name")
    IN1.IN1_12 = data.get("Plan_effective_date")
    IN1.IN1_13 = data.get("Plan_expiration_date")
    IN1.IN1_15 = data.get("plan_type")
    IN1.IN1_16 = data.get("Name_of_insured")
    IN1.IN1_17 = data.get("insured_relationship_to_patient")
    IN1.IN1_19 = data.get("insured_address")
    IN1.In1_22 = data.get("coordination_of_benefits")
    IN1.IN1_36 = data.get("policy_number")
    
    return IN1.to_er7()

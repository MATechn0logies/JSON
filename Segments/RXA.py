from hl7apy.core import Segment

def json_to_hl7_RXA(data: dict) -> str:
    rxa = Segment("RXA", version="2.5")

    rxa.RXA_1 = data.get("give_sub_id_counter")
    rxa.RXA_2 = data.get("admin_sub_id_counter")
    rxa.RXA_3 = data.get("start_datetime")
    rxa.RXA_4 = data.get("end_datetime")
    rxa.RXA_5 = data.get("administered_code")
    rxa.RXA_6 = data.get("administered_amount")
    rxa.RXA_7 = data.get("administered_units")
    rxa.RXA_8 = data.get("administered_dosage_form")
    rxa.RXA_9 = data.get("administration_notes")
    rxa.RXA_10 = data.get("administering_provider")
    rxa.RXA_11 = data.get("administered_at_location")
    rxa.RXA_12 = data.get("administered_per_time_unit")
    rxa.RXA_13 = data.get("administered_strength")
    rxa.RXA_14 = data.get("administered_strength_units")
    rxa.RXA_15 = data.get("lot_number")
    rxa.RXA_16 = data.get("expiration_date")
    rxa.RXA_17 = data.get("manufacturer_name")
    rxa.RXA_18 = data.get("refusal_reason")
    rxa.RXA_19 = data.get("indication")
    rxa.RXA_20 = data.get("completion_status")
    rxa.RXA_21 = data.get("action_code")
    rxa.RXA_22 = data.get("system_entry_datetime")

    return rxa.to_er7()

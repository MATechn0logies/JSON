from hl7apy.core import Segment
def json_to_hl7_RXO(data: dict) -> str:
    """Convert JSON to HL7 RXO segment"""
    rxo = Segment("RXO", version="2.5")

    # Set fields only if they exist in data
    if data.get("requested_give_code"):
        rxo.RXO_1 = data["requested_give_code"]
    if data.get("requested_give_amount_minimum"):
        rxo.RXO_2 = data["requested_give_amount_minimum"]
    if data.get("requested_give_amount_maximum"):
        rxo.RXO_3 = data["requested_give_amount_maximum"]
    if data.get("requested_give_units"):
        rxo.RXO_4 = data["requested_give_units"]
    if data.get("requested_dosage_form"):
        rxo.RXO_5 = data["requested_dosage_form"]
    if data.get("pharmacy_instructions"):
        rxo.RXO_6 = data["pharmacy_instructions"]
    if data.get("administration_instructions"):
        rxo.RXO_7 = data["administration_instructions"]
    if data.get("number_of_refills"):
        rxo.RXO_13 = data["number_of_refills"]
    if data.get("requested_give_per_time_unit"):
        rxo.RXO_17 = data["requested_give_per_time_unit"]
    if data.get("requested_give_rate_amount"):
        rxo.RXO_18 = data["requested_give_rate_amount"]
    if data.get("requested_give_rate_units"):
        rxo.RXO_19 = data["requested_give_rate_units"]
    if data.get("indication"):
        rxo.RXO_20 = data["indication"]
    if data.get("requested_drug_strength_values"):
        rxo.RXO_21 = data["requested_drug_strength_values"]
    if data.get("requested_drug_strength_units"):
        rxo.RXO_22 = data["requested_drug_strength_units"]
    if data.get("special_admin_instructions"):
        rxo.RXO_25 = data["special_admin_instructions"]
    if data.get("give_per_interval"):
        rxo.RXO_26 = data["give_per_interval"]

    return rxo.to_er7()  # Fixed typo: to_err() -> to_er7()
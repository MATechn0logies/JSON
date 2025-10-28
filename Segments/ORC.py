from hl7apy.core import Segment

def json_to_hl7_ORC(data: dict) -> str:
    """
    Generate an ORC (Common Order) segment from JSON data.
    Includes only fields that have values (skips empty ones).
    NABIDH-compliant minimal version.
    """
    orc = Segment("ORC", version="2.5")

    # Required minimum (defaults if missing)
    orc.ORC_1 = data.get("order_control", "RE")

    # Optional fields — only set if non-empty
    if data.get("placer_order_number"): 
        orc.ORC_2 = data["placer_order_number"]

    if data.get("filler_order_number"):
        orc.ORC_3 = data["filler_order_number"]

    if data.get("order_status"):
        orc.ORC_5 = data["order_status"]

    if data.get("quantity_timing"):
        orc.ORC_7 = data["quantity_timing"]

    if data.get("transaction_datetime"):
        orc.ORC_9 = data["transaction_datetime"]

    if data.get("entered_by"):
        orc.ORC_10 = data["entered_by"]

    if data.get("verified_by"):
        orc.ORC_11 = data["verified_by"]

    if data.get("ordering_provider"):
        orc.ORC_12 = data["ordering_provider"]

    if data.get("enterer_location"):
        orc.ORC_13 = data["enterer_location"]

    if data.get("callback_phone_number"):
        orc.ORC_14 = data["callback_phone_number"]

    if data.get("ordering_facility_name"):
        orc.ORC_21 = data["ordering_facility_name"]

    if data.get("ordering_facility_address"):
        orc.ORC_22 = data["ordering_facility_address"]

    if data.get("ordering_facility_phone"):
        orc.ORC_23 = data["ordering_facility_phone"]

    if data.get("confidentiality_code"):
        orc.ORC_28 = data["confidentiality_code"]

    if data.get("order_type"):
        orc.ORC_29 = data["order_type"]

    return orc.to_er7()

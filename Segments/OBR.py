from hl7apy.core import Segment

def json_to_hl7_OBR(data: dict) -> str:
    """
    Generate an OBR (Observation Request) segment from JSON data.
    Only includes non-empty fields (skips blanks).
    NABIDH 2.5 simplified compliant version.
    """
    obr = Segment("OBR", version="2.5")

    # --- Required fields ---
    obr.OBR_1 = data.get("set_id", "1")
    obr.OBR_2 = data.get("placer_order_number", "")
    obr.OBR_3 = data.get("filler_order_number", data.get("placer_order_number", ""))
    obr.OBR_4 = data.get("universal_service_id", "")

    # --- Optional fields (only set if value exists) ---
    if data.get("priority"):
        obr.OBR_5 = data["priority"]

    if data.get("requested_datetime"):
        obr.OBR_6 = data["requested_datetime"]

    if data.get("observation_datetime"):
        obr.OBR_7 = data["observation_datetime"]

    if data.get("specimen_action_code"):
        obr.OBR_11 = data["specimen_action_code"]

    if data.get("relevant_clinical_info"):
        obr.OBR_13 = data["relevant_clinical_info"]

    if data.get("specimen_received_datetime"):
        obr.OBR_14 = data["specimen_received_datetime"]

    if data.get("specimen_source"):
        obr.OBR_15 = data["specimen_source"]

    if data.get("ordering_provider"):
        obr.OBR_16 = data["ordering_provider"]

    if data.get("order_callback_number"):
        obr.OBR_17 = data["order_callback_number"]

    if data.get("result_status_change_datetime"):
        obr.OBR_22 = data["result_status_change_datetime"]

    if data.get("diagnostic_service_id"):
        obr.OBR_24 = data["diagnostic_service_id"]

    if data.get("result_status"):
        obr.OBR_25 = data["result_status"]

    if data.get("result_copies_to"):
        obr.OBR_28 = data["result_copies_to"]

    if data.get("reason_for_study"):
        obr.OBR_31 = data["reason_for_study"]

    if data.get("principal_result_interpreter"):
        obr.OBR_32 = data["principal_result_interpreter"]

    return obr.to_er7()

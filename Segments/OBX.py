from hl7apy.core import Segment

def json_to_hl7_OBX(data: dict) -> str:
    """
    Generate an OBX (Observation/Result) segment from JSON data.
    Only includes non-empty fields (skips blanks).
    NABIDH simplified compliant version.
    """
    obx = Segment("OBX", version="2.5")

    # --- Required ---
    obx.OBX_1 = data.get("set_id")  # Sequence number
    obx.OBX_2 = data.get("value_type")  # e.g., NM, ST, ED
    obx.OBX_3 = data.get("observation_id")

    # --- Optional fields (only set if value exists) ---
    if data.get("observation_sub_id"):
        obx.OBX_4 = data["observation_sub_id"]

    if data.get("observation_value"):
        obx.OBX_5 = data["observation_value"]

    if data.get("units"):
        obx.OBX_6 = data["units"]

    if data.get("reference_range"):
        obx.OBX_7 = data["reference_range"]

    if data.get("abnormal_flags"):
        obx.OBX_8 = data["abnormal_flags"]

    if data.get("result_status"):
        obx.OBX_11 = data["result_status"]

    if data.get("observation_datetime"):
        obx.OBX_14 = data["observation_datetime"]

    if data.get("performing_org"):
        obx.OBX_23 = data["performing_org"]

    if data.get("performing_org_address"):
        obx.OBX_24 = data["performing_org_address"]

    if data.get("performing_doctor"):
        obx.OBX_25 = data["performing_doctor"]

    return obx.to_er7()

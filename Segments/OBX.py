from hl7apy.core import Segment 
from hl7apy.core import Field

def json_to_hl7_OBX(data: dict) -> str:
    """
    Generate one OBX (Observation/Result) segment from JSON data.
    Only includes non-empty fields (skips blanks).
    NABIDH simplified compliant version.
    """
    obx = Segment("OBX", version="2.5")
    # Performing Organization Name

    # --- Required ---
    obx.OBX_1 = data.get("set_id")  # Sequence number
    obx.OBX_2 = data.get("value_type")  # e.g., NM, ST, ED
    obx.OBX_3 = data.get("observation_id")
    

    # --- Optional fields ---
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
    

        
       

   
    return obx.to_er7()


def json_to_hl7_OBX_multiple(data_list: list) -> str:
    """
    Generate multiple OBX segments if multiple observations exist.
    Automatically assigns Set IDs (OBX-1) if missing.
    """
    segments = []

    for idx, obx_data in enumerate(data_list, start=1):
        # Auto-fill OBX-1 if not provided
        if not obx_data.get("set_id"):
            obx_data["set_id"] = str(idx)
        segments.append(json_to_hl7_OBX(obx_data))

    return "\r".join(segments)

from hl7apy.core import Segment

def json_to_hl7_OBX(data: dict) -> str:
    def safe_str(value):
        if value is None:
            return ""
        return str(value)
    
    obx_fields = [""] * 23
    
    obx_fields[0] = safe_str(data.get("set_id", "1"))                    # OBX-1
    obx_fields[1] = safe_str(data.get("value_type", "ST"))               # OBX-2
    obx_fields[2] = safe_str(data.get("observation_id", ""))             # OBX-3
    obx_fields[3] = safe_str(data.get("observation_sub_id", ""))         # OBX-4
    obx_fields[4] = safe_str(data.get("observation_value", ""))          # OBX-5
    obx_fields[5] = safe_str(data.get("units", ""))                      # OBX-6
    obx_fields[6] = safe_str(data.get("reference_range", ""))            # OBX-7
    obx_fields[7] = safe_str(data.get("abnormal_flags", ""))             # OBX-8
    obx_fields[10] = safe_str(data.get("result_status", ""))             # OBX-11
    obx_fields[13] = safe_str(data.get("observation_datetime", ""))      # OBX-14
    obx_fields[22] = safe_str(data.get("performing_org", ""))            # OBX-23
    
    
    return "OBX|" + "|".join(obx_fields)
from Segments.MSH import json_to_hl7_MSH
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.ORC import json_to_hl7_ORC
from Segments.OBR import json_to_hl7_OBR
from Segments.MDMOBX import json_to_hl7_OBX
from Segments.NTE import json_to_hl7_NTE
from Segments.SPM import json_to_hl7_SPM


def json_to_hl7_oru(data: dict) -> str:
 

    segments = []

    # --- Core segments ---
    segments.append(json_to_hl7_MSH(data))
    segments.append(json_to_hl7_PID(data))
    segments.append(json_to_hl7_PV1(data))

    # --- Required ORC ---
    if not data.get("ORC"):
        raise Exception("❌ ORC segment required for ORU message")
    segments.append(json_to_hl7_ORC(data["ORC"]))

    # --- Required OBR ---
    if not data.get("OBR"):
        raise Exception("❌ OBR segment required for ORU message")
    segments.append(json_to_hl7_OBR(data["OBR"]))

    # --- OBX (one or more) ---
    if data.get("OBX"):
        for obx_item in data["OBX"]:
            segments.append(json_to_hl7_OBX(obx_item))

    # --- Optional NTE list ---
    if data.get("NTE"):
        for nte_item in data["NTE"]:
            nte_segment = json_to_hl7_NTE(nte_item)
            segments.append(nte_segment)

    # --- Optional SPM list ---
    if "SPM" in data and isinstance(data["SPM"], list):
        for spm_item in data["SPM"]:
            spm_str = json_to_hl7_SPM(spm_item)
            if spm_str:
                segments.append(spm_str)

    # --- Final HL7 message ---
    return "\r".join([s for s in segments if s])

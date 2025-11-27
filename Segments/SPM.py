from hl7apy.core import Segment

def json_to_hl7_SPM(data: dict) -> str:
    spm = Segment("SPM", version="2.5")

    spm.SPM_1 = data.get("set_id", "")
    spm.SPM_2 = data.get("specimen_id", "")
    spm.SPM_4 = data.get("specimen_type", "")
    spm.SPM_7 = data.get("specimen_collection_method", "")
    spm.SPM_8 = data.get("specimen_source_site", "")
    spm.SPM_17 = data.get("specimen_collection_datetime", "")
    spm.SPM_18 = data.get("specimen_received_datetime", "")
    return spm.to_er7()

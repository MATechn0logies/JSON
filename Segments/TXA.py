from hl7apy.core import Segment

def json_to_hl7_TXA(data: dict) -> str:
    txa = Segment("TXA", version="2.5")

    txa.TXA_1 = data.get("set_id", "1")
    txa.TXA_2 = data.get("document_type", "")
    txa.TXA_4 = data.get("activity_datetime", "")
    txa.TXA_5 = data.get("primary_activity_provider", "")
    txa.TXA_7 = data.get("transcription_datetime", "")
    txa.TXA_9 = data.get("originator", "")
    txa.TXA_12 = data.get("document_number", "")
    txa.TXA_16 = data.get("document_file_name", "")
    txa.TXA_17 = data.get("document_completion_status", "")
    txa.TXA_19 = data.get("document_availability_status", "")
    txa.TXA_22 = data.get("authentication_timestamp", "")

    return txa.to_er7()

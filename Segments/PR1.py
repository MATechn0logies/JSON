from hl7apy.core import Segment

def json_to_hl7_PR1(data: dict) -> str:

    pr1 = Segment("PR1", version="2.5")

    # Required fields
    pr1.PR1_1 = data.get("set_id", "")  # Sequence number
    pr1.PR1_3 = data.get("procedure_code", "")  # CE format: Code^Text^System
    pr1.PR1_4 = data.get("procedure_description", "")  # Text
    pr1.PR1_5 = data.get("procedure_datetime", "")  # TS

    # Optional
    if data.get("surgeon"):
        pr1.PR1_11 = data["surgeon"]
    if data.get("procedure_priority"):
        pr1.PR1_14 = data["procedure_priority"]
    if data.get("procedure_identifier"):
        pr1.PR1_19 = data["procedure_identifier"]
    if data.get("procedure_action_code"):
        pr1.PR1_20 = data["procedure_action_code"]

    return pr1.to_er7()

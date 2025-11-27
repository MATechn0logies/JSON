from hl7apy.core import Segment

def json_to_hl7_PRB(data: dict) -> str:
    """
    Generate PRB (Problem) Segment for NABIDH PPR^PC1
    Accepts  for problem deletion.
    """

    # If deletion instruction: PRB|"""" (special NABIDH case)
    if data.get("delete_all") == True:
        return 'PRB|""""'

    prb = Segment("PRB", version="2.5")

    # --- Required ---
    prb.PRB_1 = data.get("set_id")                          # Sequence number
    prb.PRB_2 = data.get("action_datetime")                # TS format
    prb.PRB_3 = data.get("problem_id")                     # Code^Text^System (CE)
    prb.PRB_4 = data.get("problem_instance_id")            # EI unique ID
    prb.PRB_7 = data.get("problem_established_date")       # Problem start date
    prb.PRB_9 = data.get("problem_resolution_date")        # Optional
    prb.PRB_10 = data.get("classification")                # F^Final^LOCALCODE
    prb.PRB_14 = data.get("life_cycle_status")             # SNOMED Code
    prb.PRB_15 = data.get("status_datetime")               # same as PRB-2
    prb.PRB_16 = data.get("problem_onset_date")            # same as PRB-7

    return prb.to_er7()

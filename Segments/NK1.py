from hl7apy.core import Segment
from typing import List, Dict

def json_to_hl7_NK1(data: Dict) -> str:
    """
    Generate one or more NK1 segments from JSON data.
    Expected input: data['NK1'] = [ {NK1 fields...}, ... ]
    """
    nk1_segments = []

    nk1_list = data.get("NK1", [])
    if not nk1_list:
        return ""

    for nk in nk1_list:
        nk1 = Segment("NK1", version="2.5")

        # 1. Set ID
        nk1.NK1_1 = nk.get("set_id", "1")

        # 2. Name
        nk1.NK1_2 = nk.get("name", "")

        # 3. Relationship
        nk1.NK1_3 = nk.get("relationship", "")

        # 4. Address (default if missing)
        nk1.NK1_4 = nk.get("address", "^^Dubai^Dubai^^784^H")

        # 5. Phone Number
        nk1.NK1_5 = nk.get("phone", "")

        # 7. Contact Role
        nk1.NK1_7 = nk.get("contact_role", "C^Emergency Contact^HL7131")

        nk1_segments.append(nk1.to_er7())

    return "\r".join(nk1_segments)
def json_to_hl7_NK1_multiple(data_list: List[Dict]) -> str:
    """ 
    Generate multiple NK1 segments if multiple next of kin entries exist.
    segments = []
    for nk_data in data_list:
        segments.append(json_to_hl7_NK1({"NK1": [nk_data]}))
    return "\r".join(segments)
    """
    segments = []
    for nk_data in data_list:
        segments.append(json_to_hl7_NK1({"NK1": [nk_data]}))
    return "\r".join(segments)      
    

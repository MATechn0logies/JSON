from Segments.MSH import json_to_hl7_MSH
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.IN1 import json_to_hl7_IN1
from Segments.ORC import json_to_hl7_ORC
from Segments.RXO import json_to_hl7_RXO

def json_to_hl7_OMP_O09(data: dict) -> str:
    hl7_segments = []
    
    print("DEBUG: Data keys:", data.keys())  # Debug print

    # ✅ Required segments
    hl7_segments.append(json_to_hl7_MSH(data))
    hl7_segments.append(json_to_hl7_PID(data))
    hl7_segments.append(json_to_hl7_PV1(data))

    # ✅ Optional IN1 (Insurance)
    if data.get("IN1"):
    
        hl7_segments.append(json_to_hl7_IN1(data["IN1"]))

    # ✅ Required ORC
    if not data.get("ORC"):
        raise Exception("❌ ORC segment is required for ORM_O01 message")
    
    hl7_segments.append(json_to_hl7_ORC(data["ORC"]))

    # ✅ Required RXO - FIXED
    if not data.get("RXO"):
        raise Exception("❌ RXO segment is required for ORM_O01 message")

    hl7_segments.append(json_to_hl7_RXO(data["RXO"]))  # Fixed line

    # ✅ Join segments with HL7 newline
    return "\r".join(hl7_segments)
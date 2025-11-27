from Segments.MSH import json_to_hl7_MSH
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1
from Segments.IN1 import json_to_hl7_IN1
from Segments.ORC import json_to_hl7_ORC
from Segments.RXO import json_to_hl7_RXO
from Segments.NTE import json_to_hl7_NTE

def json_to_hl7_ORM_O01(data: dict) -> str:

    segments = [
        json_to_hl7_MSH(data),
        json_to_hl7_PID(data),
        json_to_hl7_PV1(data)
    ]

    # Optional repeating insurance
    if "IN1" in data:
        for ins in data["IN1"]:
            segments.append(json_to_hl7_IN1(ins))

    # REQUIRED: Multiple orders allowed
    if "ORDERS" not in data:
        raise Exception("❌ ORDERS[] must contain {ORC + RXO}")

    for order in data["ORDERS"]:

        if "ORC" not in order:
            raise Exception("❌ Missing ORC inside an ORDERS block")
        segments.append(json_to_hl7_ORC(order["ORC"]))

        if "RXO" not in order:
            raise Exception("❌ Missing RXO inside an ORDERS block")
        segments.append(json_to_hl7_RXO(order["RXO"]))

    if data.get("NTE"):
        for nte_item in data["NTE"]:
            nte_segment = json_to_hl7_NTE(nte_item)
            segments.append(nte_segment)

    return "\r".join(segments)

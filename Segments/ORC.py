from hl7apy.core import Segment
from  datetime import datetime

def json_to_hl7_ORC(data: dict) -> str:
    orc = Segment("ORC", version="2.5")

    orc.ORC_1 = data.get("order_control")
    orc.ORC_2 = data.get("placer_order_number")
    orc.ORC_3 = data.get("filler_order_number")
    orc.ORC_5 = data.get("Order_status_id")
    orc.ORC_9 = data.get("Transaction_datetime")
    orc.ORC_12 = data.get("ordering_provider")
    orc.ORC_28 = data.get("confidentiality_code")
    orc.ORC_29 = data.get("OrderType")

    if data.get("order_effective_date_time"):
        orc.ORC_15 = data.get("order_effective_date_time")

    if data.get("Ordering_Facility_Name"):
        orc.ORC_22 = data.get("Ordering_Facility_Name")
    
    if data.get("Ordering_Facility_Address"):
        orc.ORC_22 = data.get("Ordering_Facility_Address")

    if data.get("Ordering_Facility_Phone"):
        orc.ORC_24 = data.get("Ordering_Facility_Phone")    

    return orc.to_er7()

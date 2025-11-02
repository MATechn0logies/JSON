from hl7apy.core import Segment

def json_to_hl7_OBR(data: dict) -> str:
    obr = Segment("OBR", version="2.5")

    obr.OBR_1 = data.get("set_id")
    obr.OBR_2 = data.get("placer_order_number")
    obr.OBR_3 = data.get("filler_order_number")
    obr.OBR_4 = data.get("universal_service_id")
    obr.OBR_7 = data.get("observation_datetime")
    obr.OBR_5 = data.get("Priority")

    obr.OBR_24 = data.get("Diagnostic_Service_Section_ID")
    obr.OBR_25 = data.get("result_status")
   


    if data.get("observation_datetime"):
        obr.OBR_7 = data.get("observation_datetime")
    
    if data.get("specimen_source"):
        obr.OBR_15 = data.get("specimen_source")

    if data.get("ordering_provider"):
        obr.OBR_16 = data.get("ordering_provider")
    
    if data.get("Order_Callback_Phone_Number "):
        obr.OBR_17 = data.get("Order_Callback_Phone_Number ")

    if data.get("ResultsRptStatusChngDateTime"):
        obr.OBR_22 = data.get("ResultsRptStatusChngDateTime")

    
    

    return obr.to_er7()

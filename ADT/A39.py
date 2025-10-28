from Segments.MSH import json_to_hl7_MSH
from Segments.EVN import json_to_hl7_EVN
from Segments.PID import json_to_hl7_PID
from Segments.MRG import json_to_hl7_MRG

def json_to_hl7_a39(data: dict) -> str:
  
    # Generate each segment
    msh = json_to_hl7_MSH(data)
    evn = json_to_hl7_EVN(data)
    pid = json_to_hl7_PID(data)
    mrg = json_to_hl7_MRG(data)

    # Combine segments using HL7 standard segment separator (\r)
    hl7_message = "\r\n".join([msh, evn, pid, mrg])

    return hl7_message

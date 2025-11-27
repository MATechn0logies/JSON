from Segments.MSH import json_to_hl7_MSH
from Segments.EVN import json_to_hl7_EVN
from Segments.PID import json_to_hl7_PID
from Segments.PV1 import json_to_hl7_PV1


def json_to_hl7_a31(data: dict) -> str:
    """
    Convert JSON data into HL7 ADT^A28 message.
    PV1 is optional — included only if 'patient_class' exists.
    """

    msh = json_to_hl7_MSH(data)
    evn = json_to_hl7_EVN(data)
    pid = json_to_hl7_PID(data)

    hl7_segments = [msh, evn, pid]

    # Include PV1 only if 'patient_class' exists
    if data.get("patient_class"):
        hl7_segments.append(json_to_hl7_PV1(data))

    hl7_message = "\r".join(hl7_segments)
    return hl7_message

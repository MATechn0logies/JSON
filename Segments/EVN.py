from hl7apy.core import Segment

def json_to_hl7_EVN(data: dict) -> str:
    """Generate EVN (Event Type) segment from JSON data. Works for ADT, ORU, etc."""

    evn = Segment("EVN", version="2.5")

    # EVN-1: Event Type Code — use from event, trigger_event, or default
    evn.EVN_1 = (
        data.get("event_type")
        or data.get("trigger_event")
        or data.get("event")
    )

    # EVN-2: Recorded Date/Time
    evn.EVN_2 = data.get("message_datetime")

    # EVN-6: Event Occurred (optional)
    evn.EVN_6 = data.get("event_occurred") or data.get("message_datetime")

    # EVN-7: Operator ID (e.g., SHERYAN user ID or operator)
    evn.EVN_7 = data.get("facility_code")      

    return evn.to_er7()

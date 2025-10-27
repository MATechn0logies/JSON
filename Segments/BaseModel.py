from pydantic import BaseModel
from typing import List, Optional

# ------------------- NK1 Segment -------------------
class NK1Segment(BaseModel):
    set_id: str
    name: str
    relationship: str
    address: str
    phone: str
    contact_role: str


# ------------------- OBX Segment -------------------
class OBXSegment(BaseModel):
    set_id: str
    value_type: str
    observation_id: str
    observation_value: str
    units: str
    observation_result_status: str
    date_time_of_observation: str


# ------------------- AL1 Segment -------------------
class AL1Segment(BaseModel):
    set_id: str
    allergen_type: str
    allergen_code: str
    allergy_severity: str
    reaction: Optional[str]
    identification_date: str


# ------------------- DG1 Segment -------------------
class DG1Segment(BaseModel):
    set_id: str
    diagnosis_coding_method: str
    diagnosis_code: str
    diagnosis_description: str
    diagnosis_date_time: str
    diagnosis_type: str
    diagnosis_priority: str
    diagnosing_clinician: str
    diagnosis_action_code: str


# ------------------- Main Patient Model -------------------
class PatientData(BaseModel):
    trigger_event: str  # Required (e.g., A04, A08, ORU)
    message_datetime: str
    message_control_id: str
    source_app: str
    facility_id_NABIDH: str
    facility_code: str
    profession: str
    patient_id: str
    government_id: str
    patient_name: str
    dob: str
    gender: str
    race: str
    address: str
    phone: str
    email: str
    language: str
    marital_status: str
    religion: str
    emirates_id: str
    nationality: str
    patient_class: str
    location: str
    attending_doctor: str
    referring_doctor: str
    admit_datetime: str
    discharge_datetime: Optional[str] = None

    # Nested optional segment lists
    NK1: Optional[List[NK1Segment]] = None
    OBX: Optional[List[OBXSegment]] = None
    AL1: Optional[List[AL1Segment]] = None
    DG1: Optional[List[DG1Segment]] = None

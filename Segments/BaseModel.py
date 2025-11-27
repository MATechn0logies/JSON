from pydantic import BaseModel
from typing import List, Optional

# ------------------- ORC Segment -------------------
class ORCSegment(BaseModel):                              # ORC.1
    order_control: str |None                         # ORC.2
    placer_order_number: str                   # ORC.3
    filler_order_number: str                   # ORC.4
    ordering_provider: str                     # ORC.12
    order_effective_date_time: Optional[str] = None  # ORC.15
    Order_status_id: Optional[str] = None      # ORC.5
    Transaction_datetime: Optional[str] = None  # ORC.9
    confidentiality_code: Optional[str] = None    # Custom field if needed
    OrderType: Optional[str] = None    # Custom field if needed
    Ordering_Facility_Name: Optional[str] = None  # ORC.22
    Ordering_Facility_Address: Optional[str] = None  # ORC.23
    Ordering_Facility_Phone: Optional[str] = None  # ORC.24


# ------------------- OBR Segment -------------------
class OBRSegment(BaseModel):
    set_id: str                                # OBR.1
    placer_order_number: str                   # OBR.2
    filler_order_number: str                   # OBR.3
    universal_service_id: str                  # OBR.4
    Priority: str                     # OBR.5
    observation_datetime: str     |None             # OBR.7
    ordering_provider: Optional[str] = None    # OBR.16
    specimen_source: Optional[str] = None      # OBR.15
    result_status: Optional[str] = None        # OBR.25
    Diagnostic_Service_Section_ID: Optional[str] = None  # OBR.24
    ResultsRptStatusChngDateTime: Optional[str] = None  # Custom field if needed
    result_status: Optional[str] = None        # OBR.25


# ------------------- Other Segments (Existing) -------------------
class NK1Segment(BaseModel):
    set_id: str
    name: str
    relationship: str
    address: str
    phone: str
    contact_role: str


class OBXSegment(BaseModel):
    set_id: str
    value_type: str
    observation_id: str
    observation_value: str
    units: str | None = None
    reference_range: str | None = None
    abnormal_flags: str | None = None
    observation_result_status: str | None = None
    observation_datetime: str | None = None
    performing_org: str | None = None
    performing_org_address: str | None = None
    performing_doctor: str | None = None
    result_status: str | None = None




class AL1Segment(BaseModel):
    set_id: str
    allergen_type_code: str               
    allergen_code: str                    
    allergy_severity_code: str            
    allergy_reaction: str                 
    identification_date: str             
    delete_all: Optional[bool] = False    



class DG1Segment(BaseModel):
    set_id: str
    diagnosis_coding_method: Optional[str] = "I10"
    diagnosis_code: str
    diagnosis_description: str
    diagnosis_datetime: str
    diagnosis_type: Optional[str] = "F"
    diagnosis_priority: Optional[str] = "1"
    diagnosing_clinician: Optional[str] = None
    diagnosis_action_code: Optional[str] = "A"



class NTESegment(BaseModel):
    set_id: str                     # NTE-1
    comment: str                    # NTE-3


class TXASegment(BaseModel):
    set_id: str
    document_type: str
    activity_datetime: str
    primary_activity_provider: str
    transcription_datetime: str
    originator: str
    document_number: str
    document_file_name: str
    document_completion_status: str
    document_availability_status: str
    authentication_timestamp: str


class IN1Segment(BaseModel):
    set_id: str                                 # IN1-1
    insurance_plan_id: str                         # IN1-2  CE  e.g. 12345^NATIONAL INSURANCE^HL7072
    insurance_company_id: str                   # IN1-3  CX  e.g. AXA^^^DHA
    insurance_company_name: str                 # IN1-4  XON e.g. AXA Insurance^L
    insurance_company_address: Optional[str] = ""  # IN1-5  XAD
    insurance_contact_person: Optional[str] = ""   # IN1-6  XPN
    insurance_co_contact_person :Optional[str] = ""  # IN1-6  XPN
    insurance_co_phone_number: Optional[str] = ""  # IN1-7  XTN
    insurance_phone: Optional[str] = ""            # IN1-7  XTN
    group_number: Optional[str] = ""               # IN1-8
    group_name: Optional[str] = ""                 # IN1-9
    Plan_effective_date: Optional[str] = ""             # IN1-12
    Plan_expiration_date: Optional[str] = ""            # IN1-13
    plan_type: Optional[str] = ""                  # IN1-15
    Name_of_insured: Optional[str] = ""               # IN1-16 XPN
    insured_relationship_to_patient: Optional[str] = ""    # IN1-17 CE
    insured_address: Optional[str] = ""            # IN1-19 XAD
    coordination_of_benefits: Optional[str] = ""     # IN1-22
    policy_number: str                     # IN1-36 (REQUIRED)


class RXOSegment(BaseModel):
    requested_give_code: str              # RXO-1
    requested_give_amount_minimum: str    # RXO-2
    requested_give_amount_maximum: Optional[str] = None  # RXO-3
    requested_give_units: str             # RXO-4
    requested_dosage_form: Optional[str] = None  # RXO-5
    pharmacy_instructions: Optional[str] = None  # RXO-6
    administration_instructions: Optional[str] = None  # RXO-7
    number_of_refills: Optional[str] = None  # RXO-13
    requested_give_per_time_unit: Optional[str] = None  # RXO-17
    requested_give_rate_amount: Optional[str] = None  # RXO-18
    requested_give_rate_units: Optional[str] = None  # RXO-19
    indication: Optional[str] = None  # RXO-20
    requested_drug_strength_volume: Optional[str] = None  # RXO-21
    requested_drug_strength_units: Optional[str] = None  # RXO-22
    special_admin_instructions: Optional[str] = None  # RXO-25
    give_per_interval: Optional[str] = None  # RXO-26




class RXASegment(BaseModel):
    give_sub_id_counter: str                    # RXA-1
    admin_sub_id_counter: str                   # RXA-2
    start_datetime: str                         # RXA-3
    end_datetime: Optional[str] = ""            # RXA-4
    administered_code: str                      # RXA-5 (CE)
    administered_amount: str                    # RXA-6
    administered_units: str                     # RXA-7 (CE)
    administered_dosage_form: Optional[str] = ""# RXA-8
    administration_notes: Optional[str] = ""    # RXA-9
    administering_provider: Optional[str] = ""  # RXA-10 (XCN)
    administered_at_location: Optional[str] = ""# RXA-11
    administered_per_time_unit: Optional[str]=""# RXA-12
    administered_strength: Optional[str] = ""   # RXA-13
    administered_strength_units: Optional[str]=""# RXA-14
    lot_number: Optional[str] = ""              # RXA-15
    expiration_date: Optional[str] = ""         # RXA-16
    manufacturer_name: Optional[str] = ""       # RXA-17
    refusal_reason: Optional[str] = ""          # RXA-18
    indication: Optional[str] = ""              # RXA-19
    completion_status: str                      # RXA-20
    action_code: Optional[str] = ""             # RXA-21
    system_entry_datetime: str                  # RXA-22
# ------------------- PRB Segment -------------------


class PRBSegment(BaseModel):
    set_id: Optional[str] = None                                # PRB-1
    action_datetime: Optional[str] = None                       # PRB-2 (TS)
    problem_id: Optional[str] = None                            # PRB-3 (CE format: Code^Text^System)
    problem_instance_id: Optional[str] = None                   # PRB-4 (EI)
    problem_established_date: Optional[str] = None              # PRB-7 (TS)
    problem_resolution_date: Optional[str] = ""                 # PRB-9 (TS, optional)
    classification: Optional[str] = None                        # PRB-10 (e.g., F^Final^LOCAL)
    life_cycle_status: Optional[str] = None                     # PRB-14 (SNOMED code)
    status_datetime: Optional[str] = None                       # PRB-15 (TS)
    problem_onset_date: Optional[str] = None                    # PRB-16 (TS)

    # Special NABIDH instruction — delete all problems
    delete_all: Optional[bool] = False


class SPMSegment(BaseModel):
    set_id: str
    specimen_id: Optional[str] = None
    specimen_type: str
    specimen_collection_method: Optional[str] = None
    specimen_source_site: Optional[str] = None
    specimen_collection_datetime: str
    specimen_received_datetime: str


class PR1Segment(BaseModel):
    set_id: str                                   # PR1-1 (sequence number)
    procedure_code: str                           # PR1-3 CE e.g. 71020^X-RAY CHEST^C4
    procedure_description: str                    # PR1-4 ST
    procedure_datetime: str                       # PR1-5 TS
    surgeon: Optional[str] = None                 # PR1-11 XCN
    procedure_priority: Optional[str] = "1"       # PR1-14 ID (1 = Primary)
    procedure_identifier: Optional[str] = None    # PR1-19 EI
    procedure_action_code: Optional[str] = "A"    # PR1-20 ID (A=Add, D=Delete)


class  OrderModel(BaseModel):
    ORC: ORCSegment
    RXO: RXOSegment



# ------------------- Patient Data Wrapper -------------------
class PatientData(BaseModel):
    trigger_event: str
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

    prior_patient_id: Optional[str] = None
    prior_visit_number: Optional[str] = None
    discharge_datetime: Optional[str] = None
    discharge_disposition: Optional[str] = None




    # Optional nested segments
    NK1: Optional[List[NK1Segment]] = None
    OBX: Optional[List[OBXSegment]] = None
    AL1: Optional[List[AL1Segment]] = None
    DG1: Optional[List[DG1Segment]] = None
    PR1: Optional[List[PR1Segment]] = None
    IN1 : Optional[List[IN1Segment]]=None
    RXA : Optional[List[RXASegment]]=None
    
    
  

    # ✅ ADD THESE FOR ORU
    ORC: Optional[ORCSegment] = None
    OBR: Optional[OBRSegment] = None
    TXA: Optional[TXASegment] = None
    RXO: Optional[RXOSegment] = None
    RXA: Optional[RXASegment] = None
    PRB: Optional[List[PRBSegment]] = None
    NTE: Optional[List[NTESegment]] = None    
    SPM: Optional[List[SPMSegment]] = None
    ORDERS: Optional[List[OrderModel]] = None


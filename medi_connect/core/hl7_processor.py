from dataclasses import dataclass
from typing import Dict, Any, Optional
from pathlib import Path

@dataclass
class Patient:
    id: str
    firstname: str
    lastname: str
    birthdate: str
    gender: str

class HL7Processor:
    """HL7 message processing class"""
    
    def __init__(self):
        self.sending_facility = "MEDI_CONNECT"
        self.receiving_facility = "HOSPITAL_SYS"
    
    def create_patient(self, patient_data: Dict[str, str]) -> Patient:
        """Create Patient object from patient data"""
        return Patient(
            id=patient_data['id'],
            firstname=patient_data['firstname'],
            lastname=patient_data['lastname'],
            birthdate=patient_data['birthdate'],
            gender=patient_data['gender']
        )
    
    def create_adt_message(self, patient: Patient) -> str:
        """Create ADT message"""
        # Simple HL7 message format
        message = f"MSH|^~\\&|{self.sending_facility}|{self.receiving_facility}|||20240319||ADT^A01\r"
        message += f"PID|||{patient.id}||{patient.lastname}^{patient.firstname}||{patient.birthdate}|{patient.gender}"
        return message
    
    def parse_adt_message(self, message: str) -> Optional[Patient]:
        """HL7 mesajını ayrıştırır ve Patient nesnesine dönüştürür"""
        try:
            segments = message.split('\r')
            pid_segment = [s for s in segments if s.startswith('PID')][0]
            fields = pid_segment.split('|')
            
            name_parts = fields[5].split('^')
            return Patient(
                id=fields[3],
                lastname=name_parts[0],
                firstname=name_parts[1],
                birthdate=fields[7],
                gender=fields[8]
            )
        except Exception as e:
            print(f"Mesaj ayrıştırma hatası: {e}")
            return None

    def save_hl7_message(self, message: str, filename: str, data_dir: Path) -> bool:
        """Save HL7 message to file"""
        try:
            # Create data_dir if not exists
            data_dir.mkdir(parents=True, exist_ok=True)
            
            # Create file path
            file_path = data_dir / filename
            
            # Write message to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(message)
                
            print(f"HL7 message saved: {file_path}")
            return True
            
        except Exception as e:
            print(f"HL7 message save error: {e}")
            return False

    def load_hl7_message(self, file_path: Path) -> Optional[str]:
        """Read HL7 message from file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
                
        except Exception as e:
            print(f"HL7 message read error: {e}")
            return None

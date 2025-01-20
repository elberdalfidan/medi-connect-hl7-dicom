from dataclasses import dataclass
from pathlib import Path

@dataclass
class Config:
    """Application configuration"""
    PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
    HL7_VERSION: str = "2.5"
    SENDING_FACILITY: str = "MEDI_CONNECT"
    RECEIVING_FACILITY: str = "HOSPITAL_SYS" 
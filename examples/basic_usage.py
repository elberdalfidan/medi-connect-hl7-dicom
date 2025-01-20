from pathlib import Path
import pydicom
from datetime import datetime
from medi_connect.core.hl7_processor import HL7Processor
from medi_connect.core.dicom_processor import DicomProcessor
from medi_connect.utils.config import Config

def demonstrate_hl7():
    print("\n=== HL7 Processing ===")
    
    # Config and HL7 processor create
    config = Config()
    hl7_proc = HL7Processor()
    
    # Example patient data
    patient_data = {
        'id': '12345',
        'firstname': 'John',
        'lastname': 'Doe',
        'birthdate': '19800101',
        'gender': 'M'
    }
    
    # Patient object create
    patient = hl7_proc.create_patient(patient_data)
    print(f"\nCreated patient: {patient}")
    
    # HL7 message create
    message = hl7_proc.create_adt_message(patient)
    print(f"\nCreated HL7 message:\n{message}")
    
    # Message save
    data_dir = config.PROJECT_ROOT / "data" / "hl7_samples"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"adt_message_{timestamp}.hl7"
    
    if hl7_proc.save_hl7_message(message, filename, data_dir):
        # Saved message read
        saved_message = hl7_proc.load_hl7_message(data_dir / filename)
        if saved_message:
            # Parsed message read
            parsed_patient = hl7_proc.parse_adt_message(saved_message)
            print(f"\nSaved and read patient data: {parsed_patient}")

def demonstrate_dicom():
    print("\n=== DICOM Processing ===")
    
    # DICOM processor create
    dicom_proc = DicomProcessor()
    
    # Example DICOM file load
    sample_path = Path(pydicom.data.get_testdata_files('CT_small.dcm')[0])
    print(f"\nDICOM file loading: {sample_path}")
    
    ds = dicom_proc.load_file(sample_path)
    if ds:
        # Metadata extract
        metadata = dicom_proc.extract_metadata(ds)
        print(f"\nDICOM Metadata:\n{metadata}")
        
        # Image extract and save
        image = dicom_proc.extract_image(ds)
        if image:
            output_path = Path('output.png')
            image.save(output_path)
            print(f"\nImage saved: {output_path}")

def main():
    print("MediConnect HL7/DICOM Toolkit Example Usage")
    print("=" * 50)
    
    try:
        demonstrate_hl7()
        demonstrate_dicom()
    except Exception as e:
        print(f"\nError occurred: {e}")

if __name__ == "__main__":
    main() 
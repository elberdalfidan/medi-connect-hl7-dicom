# MediConnect HL7/DICOM Toolkit

MediConnect is a Python toolkit for processing HL7 (Health Level 7) messages and DICOM (Digital Imaging and Communications in Medicine) files. This toolkit provices a simple and efficient way to handle healthcare data formats.

## Features

### HL7 Processing
- Create and parse ADT (Admission, Discharge, Transfer) messages
- Patient data management
- Message validation and parsing
- Save and load HL7 messages

### DICOM Processing
- Load and process DICOM files
- Extract metadata information
- Image extraction and conversion
- Support for various DICOM formats

## Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Setup

#### Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate # Unix/MacOS
```
#### or

```bash
.venv\Scripts\activate # Windows
```

#### Install package in DEvelopment mode

```bash
pip install -e .
```

## Usage

### Basic HL7 Example

```bash
from medi_connect.core.hl7_processor import HL7Processor
```
#### Initialize HL7Processor

```bash
hl7_processor = HL7Processor()
```

#### Create patient data

```bash
patient_data = {
    "id": "12345",
    "firstname": "John",
    "lastname": "Doe",
    "gender": "M",
    "birthdate": "19900101"
}
```

#### Create and process HL7 message

```bash
patient = hl7_processor.create_patient(patient_data)
message = hl7_proc.create_adt_message(patient)
```


### Basic DICOM Example
```bash
from pathlib import Path
from medi_connect_core.dicom_processor import DicomProcessor
```

#### Initialize processor
```bash
dicom_processor = DicomProcessor()
```

#### Load and process DICOM file
```bash
file_path = Path('path/to/dicom/file.dcm')
ds = dicom_proc.load_file(file_path)
metadata = dicom_proc.extract_metadata(ds)
image = dicom_proc.extract_image(ds)
```

## Project Structure
    .
    medi-connect-hl7-dicom/
    ├── medi_connect/ # Main package
    │ ├── core/ # Core functionality
    │ │ ├── hl7_processor.py
    │ │ └── dicom_processor.py
    │ └── utils/ # Utilities
    │ └── config.py
    ├── examples/ # Usage examples
    ├── data/ # Data directory
    │ ├── hl7_samples/ # HL7 message samples
    │ └── dicom_samples/ # DICOM file samples
    └── tests/ # Test suite

## Development

### Settings up Development Environment

```bash
pip install -r requirements.txt
```









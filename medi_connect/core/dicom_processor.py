from dataclasses import dataclass
from typing import Optional, Dict, Any
from pathlib import Path
import pydicom
from PIL import Image
import numpy as np

@dataclass
class DicomMetadata:
    patient_id: str
    patient_name: str
    study_date: str
    modality: str

class DicomProcessor:
    """DICOM file processing class"""
    
    def load_file(self, file_path: Path) -> Optional[pydicom.dataset.FileDataset]:
        """Load DICOM file"""
        try:
            return pydicom.dcmread(file_path)
        except Exception as e:
            print(f"DICOM file read error: {e}")
            return None
    
    def extract_metadata(self, ds: pydicom.dataset.FileDataset) -> Optional[DicomMetadata]:
        """Extract metadata from DICOM file"""
        try:
            return DicomMetadata(
                patient_id=getattr(ds, 'PatientID', 'Unknown'),
                patient_name=str(getattr(ds, 'PatientName', 'Unknown')),
                study_date=getattr(ds, 'StudyDate', 'Unknown'),
                modality=getattr(ds, 'Modality', 'Unknown')
            )
        except Exception as e:
            print(f"Metadata extraction error: {e}")
            return None
    
    def extract_image(self, ds: pydicom.dataset.FileDataset) -> Optional[Image.Image]:
        """Extract image from DICOM file"""
        try:
            # Convert pixel data to numpy array
            pixel_array = ds.pixel_array
            
            # Image normalization
            if pixel_array.max() > 0:
                pixel_array = pixel_array / pixel_array.max() * 255
            
            # Convert to 8-bit unsigned integer
            pixel_array = pixel_array.astype(float)
            scaled_array = ((pixel_array - pixel_array.min()) / 
                          (pixel_array.max() - pixel_array.min()) * 255.0)
            output_array = np.uint8(scaled_array)
            
            # Convert to PIL Image
            return Image.fromarray(output_array)
        except Exception as e:
            print(f"Image extraction error: {e}")
            return None

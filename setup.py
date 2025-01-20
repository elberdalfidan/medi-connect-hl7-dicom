from setuptools import setup, find_packages

setup(
    name="medi_connect",
    version="0.1.0",
    description="HL7 and DICOM processing toolkit",
    packages=find_packages(),
    install_requires=[
        'hl7==0.4.1',
        'pydicom==2.3.1',
        'Pillow>=10.0.0',
        'numpy>=1.24.3',
    ],
    python_requires='>=3.11',
)

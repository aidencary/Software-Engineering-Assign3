# Patient Registry System

A simple patient record management system that demonstrates Design Realization principles by translating software requirements into functional code with full traceability.

- Google Doc link to report
  - https://docs.google.com/document/d/13aECFGq0OhhfOrgOAeFHFJJXbwxT4WJCn6v-0xZ7QdI/edit?usp=sharing

## Features

This system implements the following requirements:

- **REQ-01**: Create new patient records with unique IDs (P-101, P-102, etc.)
- **REQ-02**: Retrieve patient records using their unique Patient ID
- **REQ-03**: Ensure data integrity by preventing Patient ID modification
- **REQ-04**: Update patient names while keeping their ID unchanged
- **REQ-05**: Delete patient records with appropriate error handling

### Core Functionality

- Register new patients with automatic ID generation
- Search and retrieve patient information by ID
- Update patient names (ID remains immutable)
- Delete patient records
- List all registered patients
- Input validation and error handling
- Two-tier menu system (Main Menu → Application Menu)

## File Structure

```
Software-Engineering-Assign3/
│
├── main.py                  # Menu-driven user interface
├── patient_registry.py      # PatientRegistry class implementation
├── test_patient.py          # Unit tests for all requirements
├── README.md                # Project documentation
│
├── docs/
│   └── CSCI 4490_Practice_2_Requirements to Design to Implementation(1).pdf
│
└── __pycache__/             # Python cache files
```

## Usage

Run the application:
```bash
python main.py
```

### Menu Navigation

**Main Menu:**
1. Run Application
2. Exit

**Patient Registry Menu:**
1. Register a new patient
2. Retrieve patient by ID
3. Update patient name (ID cannot be changed)
4. Delete patient by ID
5. List all patients
6. Go back to the main

## Requirements

- Python 3.x

## Testing

Run unit tests:
```bash
python test_patient.py
```

Or run tests automatically before the application:
```bash
python main.py
```

## Implementation Principles

- **Readability**: PEP8 compliant with descriptive naming conventions
- **Single Responsibility**: PatientRegistry handles only patient data management
- **Encapsulation**: Patient data stored in private dictionary with public interface
- **Traceability**: All methods tagged with requirement comments (# REQ-01, etc.)
- **Error Handling**: Comprehensive validation and error messages

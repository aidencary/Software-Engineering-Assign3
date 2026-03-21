# Patient Registry System

## Project Overview

The **Simple Patient Record System (SPRS)** is an educational software project designed to demonstrate the complete software development lifecycle, from requirements engineering through design to implementation. This system showcases how to systematically translate software requirements into high-quality, maintainable code while maintaining strict traceability between requirements, design, and implementation.

### System Description

The SPRS is a command-line application that manages basic patient medical records. It provides a user-friendly, menu-driven interface for healthcare administrators to perform essential patient data operations. The system uses a dictionary-based data structure to simulate a database, making it lightweight and educational while maintaining realistic functionality.

**Key Capabilities:**
- Create and store patient records with auto-generated unique identifiers
- Retrieve patient information using their Patient ID
- Update patient information while maintaining data integrity
- Delete patient records with proper error handling
- List all registered patients in the system
- Comprehensive input validation and error messaging

- Google Doc link to report
  - https://docs.google.com/document/d/13aECFGq0OhhfOrgOAeFHFJJXbwxT4WJCn6v-0xZ7QdI/edit?usp=sharing

### Design Approach

The system follows a **layered architecture** pattern with clear separation of concerns:

1. **Presentation Layer** (`main.py`): Handles user interaction through a 
   two-tier menu system
2. **Business Logic Layer** (`patient_registry.py`): Implements core patient 
   management operations
3. **Data Storage Layer**: Dictionary-based in-memory data structure simulating 
   a database

### Data Model

Each patient record is stored as a dictionary entry:
```python
patient_id -> {
    "patient_id": "P-101",
    "name": "John Doe"
}
```

**Key Design Decisions:**
- **Unique ID Generation**: Sequential IDs (P-101, P-102, ...) ensure 
  uniqueness and traceability
- **Immutable IDs**: Patient IDs are read-only after creation, preventing 
  data integrity issues
- **Dictionary Storage**: Provides O(1) lookup time and simulates real 
  database key-value relationships

## Requirements Specification

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
├── main.py                      # Menu-driven user interface
├── patient_registry.py          # PatientRegistry class implementation
├── test_patient_registry.py     # Unit and component tests for all requirements
├── requirements.txt             # Python dependencies (coverage)
├── README.md                    # Complete project documentation
├── .gitignore                   # Git ignore configuration
│
├── docs/
│   ├── CSCI 4490_Practice_2_Requirements to Design to Implementation(1).pdf
│   ├── SPRS_High_Level_Diagram.drawio.pdf
│   ├── SPRS_Class_Diagram.drawio.png
│   └── Component-Testing-SPRS.drawio.png  # CT-01 and CT-02 workflow diagrams
│
├── test_cases/
│   └── Software Engineering Assignment 4 - Aiden, Zach, and Keller.xlsx
│
└── target/                      # Generated — coverage report output (git-ignored)

```

## Usage

Run the application:
```bash
python main.py
```

### Menu Navigation

**Main Menu:**
1. Run Application
2. Clear terminal
3. Exit

**Patient Registry Menu:**
1. Register a new patient
2. Retrieve patient by ID
3. Update patient name (ID cannot be changed)
4. Delete patient by ID
5. List all patients
6. Clear terminal
7. Go back to the main menu

## Requirements

- Python 3.x
- coverage 7.13.5 (`pip install -r requirements.txt`)


## Testing

Run all tests (unit + component):
```bash
python -m unittest test_patient_registry -v
```

Run with coverage and generate an HTML report:
```bash
python -m coverage run -m unittest test_patient_registry
python -m coverage html -d target/htmlcov
```

### Test Suite Summary

| Class | Tests | Coverage |
|---|---|---|
| `TestPatientRegistry` | 22 unit tests + 2 component tests | REQ-01 – REQ-05, error handling, boundary values, CT-01 and CT-02 workflows |

## Implementation Principles

This project exemplifies professional software engineering practices:

### Code Quality Standards

- **Readability**: PEP8 compliant with descriptive naming conventions
- **Single Responsibility**: PatientRegistry handles only patient data 
  management; main.py handles only user interaction
- **Encapsulation**: Patient data stored in private dictionary with public 
  interface methods
- **Traceability**: All methods tagged with requirement comments 
  (# REQ-01, etc.)
- **Self-Documenting Code**: Clear method names, comprehensive docstrings, 
  and inline comments
- **Error Handling**: Comprehensive validation and user-friendly error messages

### Testing Strategy

- **Unit Testing**: 22 test cases covering all requirements (REQ-01 through REQ-05)
- **Component Testing**: 2 multi-step workflow tests (CT-01 register→update→retrieve, CT-02 register→delete→retrieve) verifying method interactions across REQ-01 through REQ-05
- **Equivalence Partitioning**: 10 partitions across `name` and `patient_id` inputs
- **Boundary Value Analysis**: 3-point BVA on name length and patient ID numeric boundaries
- **Decision Table Testing**: All condition/effect combinations for each method
- **Edge Case Testing**: Invalid inputs, non-existent records, empty data
- **Error Path Testing**: Validates proper exception handling
- **Coverage Analysis**: Statement, branch, and condition coverage annotations on all tests; 100% statement coverage of `patient_registry.py`
- **Total Test Cases**: 24 automated tests in `TestPatientRegistry`

## Member Contributions

### Assignment 3 (Design & Implementation)

#### Aiden Cary
- Created initial main.py and patient_registry.py
- Implemented REQ-01 (patient registration) and REQ-02 (patient retrieval)
- Implemented print_patients() method for listing all records
- Created print menu helper methods
- Designed and implemented a two-tier menu system
- Refactored patient registry
- Created and updated the README with comprehensive documentation
- Added and improved error handling throughout the application
- Added screenshot evidence to the report
- Ensured PEP8 compliance across all files

#### Zach Atchley
- Helped create test_patient.py test suite
- Implemented REQ-04 requirement (update patient name functionality)
- Implemented the REQ-05 requirement (delete patient record functionality)
- Created test cases for the update_patient_name() method
- Created test cases for the delete_patient() method
- Developed error handling tests for non-existent patients
- Contributed to method return type specifications
- Tested edge cases for deletion operations
- Created High-Level Architecture diagram

#### Keller Willhite
- Helped create test_patient.py test suite
- Finalized test_patient.py test suite with all 10 tests
- Created comprehensive test cases for all requirements (REQ-01 through REQ-05)
- Implemented validation tests (invalid names, invalid ID formats)
- Developed test cases for error handling scenarios
- Ensured 100% test coverage of all public methods
- Validated data integrity through testing
- Documented test requirement traceability with comments
- Created class diagram

### Assignment 4 (Testing Phase)

#### Aiden Cary
- Merged and resolved conflicts from Zach's PR #2 (test refactor branch)
- Integrated comprehensive unit test suite: normal, edge, boundary, and invalid-input scenarios across all requirements
- Added `print_patients()` back to `patient_registry.py` after it was removed during merge
- Added `KeyError` guard to `update_patient_name()` for non-existent patient IDs
- Added statement, branch, and condition coverage annotations to all test comments
- Renamed component tests to descriptive names (`test_component_register_update_retrieve`, `test_component_register_delete_retrieve_fails`)
- Added `requirements.txt` with `coverage` dependency
- Created Component-Testing-SPRS.drawio.png diagram illustrating CT-01 and CT-02 workflows
- Updated README to reflect Assignment 4 testing structure

#### Zach Atchley
- Refactored test suite: replaced `test_patient.py` with `test_patient_registry.py`
- Implemented component tests CT-01 (register→update→retrieve) and CT-02 (register→delete→retrieve)
- Removed `print_patients()` method and `__main__` block from `patient_registry.py`
- Helped implement unit tests (Phase 2): normal, edge, boundary, and invalid-input scenarios

#### Keller Willhite
- Helped implement all unit tests (Phase 2): normal, edge, boundary, and invalid-input scenarios

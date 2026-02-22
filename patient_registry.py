# patient_registry.py
# PatientRegistry class for managing patient records.
class PatientRegistry:
    # Constructor
    def __init__(self):
        self.patients = {}
        # 101 is the starting patient ID which is incremented for each new patient registration
        self.patient_id = "P-101"

    # Method to register a new patient
    def register_patient(self, name: str) -> str:
        """
        Registers a new patient and returns the assigned patient ID.
        Avoids duplicate patient IDs by incrementing the patient ID for each new registration.
        Validates that the name is a non-empty string.
        """
        if not isinstance(name, str) or name == "":
            raise ValueError("Name must be a non-empty string")

        # REQ-01: Generate unique patient ID and store patient information
        # REQ-03 Prevent modification of Patient ID after assignment (setter is not provided)
        current_id = self.patient_id
        self.patients[current_id] = {"name": name}
        self.patient_id = str(int(self.patient_id.split("-")[1]) + 1)
        self.patient_id = f"P-{self.patient_id}"

        return current_id

    # Gets the patient information by patient ID key
    def get_patient(self, patient_id: str) -> dict:
        """
        Retrieves patient information by patient ID.
        Returns an error message if patient ID does not exist.
        """
        # REQ-02: Retrieve patient information by ID with error handling for non-existent IDs
        pid = str(patient_id).strip("P-")
        if not pid.isdigit() or int(pid) < 101:
            raise ValueError("Invalid patient ID format")
        
        if patient_id not in self.patients:
            raise KeyError("Patient ID does not exist")

        return self.patients[patient_id]
    
    # Print all registered patients
    def print_patients(self):
        """
        Prints all registered patients in a readable format.
        """
        if not self.patients:
            print("No patients registered.")
            return
        
        for pid, info in self.patients.items():
            print(f"Patient ID: {pid}, Name: {info['name']}")
    
if __name__ == "__main__":
    registry = PatientRegistry()
    print("Registering patients...")
    registry.register_patient("Alice")
    registry.register_patient("Bob")
    registry.print_patients()
            
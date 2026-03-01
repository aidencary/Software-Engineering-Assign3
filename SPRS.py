# SPRS.py
# Simple Patient Record System - Complete Source Code
# This file contains all source code for the Patient Registry System

import os

# ============================================================================
# PatientRegistry Class - Core Business Logic
# ============================================================================

class PatientRegistry:
    """
    PatientRegistry class for managing patient records.
    Implements requirements REQ-01 through REQ-05.
    """

    def __init__(self):
        """Initialize the PatientRegistry with an empty patient dictionary."""
        self.patients = {}
        # 101 is the starting patient ID which is incremented for
        # each new patient registration
        self.patient_id = "P-101"

    def register_patient(self, name: str) -> str:
        """
        Registers a new patient and returns the assigned patient ID.
        Avoids duplicate patient IDs by incrementing the patient ID for
        each new registration. Validates that the name is a non-empty
        string.

        Args:
            name: The name of the patient to register

        Returns:
            str: The assigned patient ID

        Raises:
            ValueError: If name is not a non-empty string
        """
        if not isinstance(name, str) or name == "":
            raise ValueError("Name must be a non-empty string")

        # REQ-01: Generate unique patient ID and store patient info
        # REQ-03: Prevent modification of Patient ID after assignment
        current_id = self.patient_id
        self.patients[current_id] = {"patient_id": current_id, "name": name}
        self.patient_id = str(int(self.patient_id.split("-")[1]) + 1)
        self.patient_id = f"P-{self.patient_id}"

        return current_id

    def get_patient(self, patient_id: str) -> dict:
        """
        Retrieves patient information by patient ID.
        Returns an error message if patient ID does not exist.

        Args:
            patient_id: The ID of the patient to retrieve

        Returns:
            dict: Patient record containing patient_id and name

        Raises:
            ValueError: If patient_id format is invalid
            KeyError: If patient_id does not exist
        """
        # REQ-02: Retrieve patient information by ID with error
        # handling for non-existent IDs
        pid = str(patient_id).strip("P-")
        if not pid.isdigit() or int(pid) < 101:
            raise ValueError("Invalid patient ID format")

        if patient_id not in self.patients:
            raise KeyError("Patient ID does not exist")

        return self.patients[patient_id]

    def print_patients(self):
        """
        Prints all registered patients in a readable format.
        """
        if not self.patients:
            print("No patients registered.")
            return

        for pid, info in self.patients.items():
            print(f"Patient ID: {pid}, Name: {info['name']}")

    def update_patient_name(self, patient_id: str, name: str) -> dict:
        """
        Updates the name associated with the given patient ID.
        Returns the updated patient record.

        Args:
            patient_id: The ID of the patient to update
            name: The new name for the patient

        Returns:
            dict: Updated patient record

        Raises:
            ValueError: If name is not a non-empty string
        """
        # REQ-04: Update patient name with patient ID
        # (ID remains unchanged)
        if not isinstance(name, str) or name == "":
            raise ValueError("Name must be a non-empty string")
        self.patients[patient_id] = {"patient_id": patient_id, "name": name}
        return self.patients[patient_id]

    def delete_patient(self, patient_id: str) -> bool:
        """
        Deletes the patient record with the corresponding patient ID.
        Returns True if deletion was successful.

        Args:
            patient_id: The ID of the patient to delete

        Returns:
            bool: True if deletion was successful

        Raises:
            KeyError: If patient_id does not exist
        """
        # REQ-05: Delete patient using Patient ID
        del self.patients[patient_id]
        return True


# ============================================================================
# User Interface Functions - Presentation Layer
# ============================================================================

def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_registry_menu():
    """Prints the patient registry menu and returns the user's choice."""
    print("\n--- Patient Registry System ---")
    print("1. Register a new patient")
    print("2. Retrieve patient by ID")
    print("3. Update patient name (ID cannot be changed)")
    print("4. Delete patient by ID")
    print("5. List all patients")
    print("6. Clear terminal")
    print("7. Go back to the main menu")
    choice = input("Enter your choice: ")
    return choice.strip()


def patient_registry_menu(registry):
    """
    Submenu for Patient Registry operations.

    Args:
        registry: PatientRegistry instance to operate on
    """
    while True:

        # Display the patient registry menu and get user choice
        choice = print_registry_menu()

        # Register a new patient
        if choice == '1':
            name = input("Enter patient's name: ")
            try:
                patient_id = registry.register_patient(name)
                print(f"Patient registered with ID: {patient_id}")
            except ValueError as e:
                print(f"Error: {e}")
        # Retrieve patient by ID
        elif choice == '2':
            patient_id = input("Enter patient ID (e.g., P-101): ")
            try:
                patient_info = registry.get_patient(patient_id)
                print(f"Patient ID: {patient_id}, "
                      f"Name: {patient_info['name']}")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
        # Update patient name
        elif choice == '3':
            try:
                patient_id = input("Enter patient ID (e.g., P-101): ")
                registry.get_patient(patient_id)

                name = input("Enter new patient name: ")
                updated_record = registry.update_patient_name(patient_id,
                                                              name)

                print(f"Updated Patient - ID: {updated_record['patient_id']}"
                      f", Name: {updated_record['name']}")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
        # Delete patient by ID
        elif choice == '4':
            try:
                patient_id = input("Enter patient ID (e.g., P-101): ")
                registry.get_patient(patient_id)
                result = registry.delete_patient(patient_id)

                if result:
                    print(f"Successfully deleted patient record with ID: "
                          f"{patient_id}")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
        # List all patients
        elif choice == '5':
            registry.print_patients()
        # Clear terminal
        elif choice == '6':
            clear_terminal()
        # Go back to the main menu
        elif choice == '7':
            print("Returning to main menu...")
            break
        # Invalid choice handling
        else:
            print("Invalid choice. Please choose 1-7.")


def print_main_menu():
    """Prints the main menu and returns the user's choice."""
    print("\n=== Main Menu ===")
    print("1. Run Application")
    print("2. Clear terminal")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice.strip()


def run_app():
    """
    Main menu for the application.
    Entry point for the Patient Registry System.
    """
    # Create an instance of PatientRegistry
    registry = PatientRegistry()

    while True:
        # Display the main menu and get user choice
        choice = print_main_menu()

        if choice == '1':
            patient_registry_menu(registry)

        elif choice == '2':
            clear_terminal()

        elif choice == '3':
            print("Exiting the Patient Registry System.")
            break

        else:
            print("Invalid choice. Please choose 1-3.")


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Simple Patient Record System (SPRS)")
    print("Version 1.0")
    print("=" * 60)
    run_app()

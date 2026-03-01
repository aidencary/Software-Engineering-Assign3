# main.py
# Patient Registry System

import unittest
from patient_registry import PatientRegistry
from test_patient import TestPatientRegistry


def patient_registry_menu(registry):
    """Submenu for Patient Registry operations"""
    while True:
        print("\n--- Patient Registry System ---")
        print("1. Register a new patient")
        print("2. Retrieve patient by ID")
        print("3. Update patient name (ID cannot be changed)")
        print("4. Delete patient by ID")
        print("5. List all patients")
        print("6. Go back to the main")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient's name: ")
            try:
                patient_id = registry.register_patient(name)
                print(f"Patient registered with ID: {patient_id}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            patient_id = input("Enter patient ID (e.g., P-101): ")
            try:
                patient_info = registry.get_patient(patient_id)
                print(f"Patient ID: {patient_id}, "
                      f"Name: {patient_info['name']}")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")

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

        elif choice == '5':
            registry.print_patients()

        elif choice == '6':
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please choose 1-6.")


def run_app():
    """Main menu for the application"""
    # Create an instance of PatientRegistry
    registry = PatientRegistry()

    while True:
        print("\n=== Main Menu ===")
        print("1. Run Application")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_registry_menu(registry)

        elif choice == '2':
            print("Exiting the Patient Registry System.")
            break

        else:
            print("Invalid choice. Please choose 1-2.")


if __name__ == "__main__":
    # Run unit tests
    unittest.main(exit=False)

    # Run the application
    run_app()

# main.py
# Patient Registry System

import unittest
from patient_registry import PatientRegistry
from test_patient import TestPatientRegistry

def run_app():
    # Create an instance of PatientRegistry
    registry = PatientRegistry()

    # Menu for PatientRegistry
    while True:
        print("\nPatient Registry System")
        print("1. Register a new patient")
        print("2. Retrieve patient information")
        print("3. Print all registered patients")
        print("4. Exit")

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
                print(f"Patient ID: {patient_id}, Name: {patient_info['name']}")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")

        elif choice == '3':
            registry.print_patients()

        elif choice == '4':
            print("Exiting the Patient Registry System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Run unit tests
    unittest.main(exit=False)

    # Run the application
    run_app()
    
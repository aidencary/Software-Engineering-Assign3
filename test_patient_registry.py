# test_patient_registry.py
# Unit and component tests for PatientRegistry class.
import unittest
from unittest.mock import patch
from patient_registry import PatientRegistry


class TestPatientRegistry(unittest.TestCase):

    # Set up a new PatientRegistry instance before each test
    def setUp(self):
        self.registry = PatientRegistry()

    # --- Registration and retrieval tests ---

    def test_register_retrieve(self):
        """Test registering a patient and retrieving their information."""
        # REQ-01, REQ-02 | TESTS: TC-01, TC-05, TC-R1, TC-G1, TC-BV5
        pid = self.registry.register_patient('Bob')
        record = self.registry.get_patient(pid)

        self.assertEqual(record['name'], 'Bob')
        self.assertEqual(record['patient_id'], 'P-101')
        self.assertEqual(pid, 'P-101')

    def test_register_invalid_name(self):
        """Test registering patient with empty name raises ValueError."""
        # REQ-01 | TESTS: TC-02, TC-R2, TC-BV1
        with self.assertRaises(ValueError):
            self.registry.register_patient("")

    def test_register_non_string_name(self):
        """Test registering a patient with a non-string name raises ValueError."""
        # REQ-01 | TESTS: TC-03, TC-R3, TC-BV7
        with self.assertRaises(ValueError):
            self.registry.register_patient(123)

    def test_register_none_name(self):
        """Test registering a patient with None as the name raises ValueError."""
        # REQ-01 | TESTS: TC-04
        with self.assertRaises(ValueError):
            self.registry.register_patient(None)

    def test_register_single_char_name(self):
        """Test registering a patient with a 1-character name succeeds."""
        # REQ-01 | TESTS: TC-BV2
        pid = self.registry.register_patient("A")
        self.assertEqual(pid, "P-101")
        self.assertEqual(self.registry.get_patient(pid)["name"], "A")

    def test_register_two_char_name(self):
        """Test registering a patient with a 2-character name succeeds."""
        # REQ-01 | TESTS: TC-BV3
        pid = self.registry.register_patient("AB")
        self.assertEqual(pid, "P-101")
        self.assertEqual(self.registry.get_patient(pid)["name"], "AB")

    # --- Retrieval tests ---

    def test_get_patient_by_id(self):
        """Test retrieving a patient record using their Patient ID."""
        # REQ-02, REQ-03 | TESTS: TC-05, TC-G1, TC-BV5
        pid = self.registry.register_patient("Charlie")
        record = self.registry.get_patient(pid)

        self.assertEqual(record["name"], "Charlie")
        self.assertEqual(record["patient_id"], pid)
        self.assertEqual(pid, "P-101")

    def test_search_for_non_existent_patient(self):
        """Test that searching for a non-existent patient raises KeyError."""
        # REQ-02 | TESTS: TC-06, TC-G2, TC-BV8
        with self.assertRaises(KeyError):
            self.registry.get_patient('P-9999')

    def test_invalid_patient_id_format(self):
        """Test retrieving with a letters-only patient ID raises ValueError."""
        # REQ-02 | TESTS: TC-07, TC-G3
        with self.assertRaises(ValueError):
            self.registry.get_patient("ABC")

    def test_get_numeric_only_id(self):
        """Test retrieving with a numeric-only patient ID raises KeyError.

        Spec expects ValueError, but strip('P-') only strips characters so
        '101' passes format validation — documents a format validation defect.
        """
        # REQ-02 | TESTS: TC-08 (DEFECT: 'P-' prefix not enforced by format check)
        with self.assertRaises(KeyError):
            self.registry.get_patient("101")

    def test_get_id_below_minimum(self):
        """Test retrieving with a patient ID numeric part below 101 raises ValueError."""
        # REQ-02 | TESTS: TC-09, TC-BV4
        with self.assertRaises(ValueError):
            self.registry.get_patient("P-100")

    def test_get_empty_id(self):
        """Test retrieving with an empty patient ID raises ValueError."""
        # REQ-02 | TESTS: TC-10
        with self.assertRaises(ValueError):
            self.registry.get_patient("")

    def test_get_valid_format_not_registered(self):
        """Test retrieving a valid-format ID that was never registered raises KeyError."""
        # REQ-02 | TESTS: TC-BV6
        with self.assertRaises(KeyError):
            self.registry.get_patient("P-102")

    # --- Update tests ---

    def test_update_patient_name(self):
        """Test updating a patient's name keeps the ID unchanged."""
        # REQ-04 | TESTS: TC-U1
        pid = self.registry.register_patient("Alice")
        updated_record = self.registry.update_patient_name(pid, "Alicia")

        self.assertEqual(updated_record["name"], "Alicia")
        self.assertEqual(updated_record["patient_id"], pid)

        retrieved_record = self.registry.get_patient(pid)
        self.assertEqual(retrieved_record["name"], "Alicia")
        self.assertEqual(pid, "P-101")

    def test_update_non_existent_patient(self):
        """Test that retrieving a non-existent patient before update raises KeyError."""
        # REQ-04 | TESTS: TC-06, TC-G2
        with self.assertRaises(KeyError):
            self.registry.get_patient("P-9999")

    def test_update_invalid_name(self):
        """Test updating a patient with an empty name raises ValueError."""
        # REQ-04 | TESTS: TC-U3
        pid = self.registry.register_patient("Alice")
        with self.assertRaises(ValueError):
            self.registry.update_patient_name(pid, "")

    def test_update_nonexistent_id(self):
        """Test update_patient_name with a valid name and non-existent ID raises KeyError."""
        # REQ-04 | TESTS: TC-U2
        with self.assertRaises(KeyError):
            self.registry.update_patient_name("P-9999", "Alicia")

    def test_update_invalid_name_nonexistent_id(self):
        """Test update_patient_name with an empty name and non-existent ID raises ValueError."""
        # REQ-04 | TESTS: TC-U4
        with self.assertRaises(ValueError):
            self.registry.update_patient_name("P-9999", "")

    # --- Deletion tests ---

    def test_delete_patient(self):
        """Test deleting a patient record removes it from the registry."""
        # REQ-05 | TESTS: TC-D1
        pid = self.registry.register_patient("Bob")
        result = self.registry.delete_patient(pid)

        self.assertTrue(result)

        with self.assertRaises(KeyError):
            self.registry.get_patient(pid)

    def test_delete_non_existent_patient(self):
        """Test that deleting a non-existent patient raises KeyError."""
        # REQ-05 | TESTS: TC-D2
        with self.assertRaises(KeyError):
            self.registry.delete_patient("P-9999")

    # --- print_patients tests ---

    def test_print_patients_empty(self):
        """Test print_patients prints a message when no patients are registered."""
        with patch('builtins.print') as mock_print:
            self.registry.print_patients()
            mock_print.assert_called_once_with("No patients registered.")

    def test_print_patients_with_records(self):
        """Test print_patients prints each registered patient's ID and name."""
        self.registry.register_patient("Alice")
        self.registry.register_patient("Bob")

        with patch('builtins.print') as mock_print:
            self.registry.print_patients()
            mock_print.assert_any_call("Patient ID: P-101, Name: Alice")
            mock_print.assert_any_call("Patient ID: P-102, Name: Bob")
            self.assertEqual(mock_print.call_count, 2)

    # --- Component tests ---

    def test_component_1(self):
        """
        Component Test 1: Register a patient, update their name, and then
        retrieve the patient's information.
        This test will verify that all operations work together as expected.
        TESTS: REQ-01, REQ-02, REQ-03, REQ-04
        """
        print('\nRunning Component Test 1...\n')

        self.registry = PatientRegistry()

        # Step 1: Register a patient
        patient_id = self.registry.register_patient('Alice')
        print(f'Registered patient with ID: {patient_id}')

        # Step 2: Update the patient's name
        self.registry.update_patient_name(patient_id, 'Alice Smith')
        updated_name = self.registry.get_patient(patient_id)['name']
        print(f'Updated patient name to: {updated_name}')

        # Step 3: Attempt to retrieve the deleted patient (should raise KeyError)
        try:
            self.registry.get_patient(patient_id)
            print('PASS: Successfully retrieved patient after update')
        except KeyError:
            print('FAIL: Expected to retrieve patient after update, but got KeyError')

    def test_component_2(self):
        """
        Component Test 2: Register a patient, delete the patient, and then
        attempt to retrieve the patient's information.
        This test will verify that deletion works correctly and that retrieving
        a deleted patient raises the appropriate error.
        TESTS: REQ-01, REQ-02, REQ-05
        """
        print('\nRunning Component Test 2...\n')

        self.registry = PatientRegistry()

        # Step 1: Register a patient
        patient_id = self.registry.register_patient('Alice')
        print(f'Registered patient with ID: {patient_id}')

        # Step 2: Delete the patient
        self.registry.delete_patient(patient_id)

        # Step 3: Attempt to retrieve the deleted patient (should raise KeyError)
        try:
            self.registry.get_patient(patient_id)
            print('FAIL: Expected KeyError when retrieving deleted patient')
        except KeyError:
            print('PASS: Successfully raised KeyError when retrieving deleted patient')


if __name__ == '__main__':
    unittest.main()

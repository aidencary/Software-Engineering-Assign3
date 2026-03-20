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


class TestPatientRegistryComponents(unittest.TestCase):

    def setUp(self):
        self.registry = PatientRegistry()

    def test_component_register_update_retrieve(self):
        """
        CT-01 - Valid multi-step workflow.
        Workflow: register_patient() -> update_patient_name() -> get_patient()
        TESTS: REQ-01, REQ-03, REQ-04
        Branch coverage: False (success) paths in all three methods.
        Condition coverage: C1 (not isinstance) = False, C2 (name=="") = False.
        """
        # Step 1: register
        pid = self.registry.register_patient("Alice")
        self.assertEqual(pid, "P-101")  # REQ-01: ID starts at P-101

        # Step 2: update name
        updated = self.registry.update_patient_name(pid, "Alicia")
        self.assertEqual(updated["patient_id"], pid)   # REQ-03: ID unchanged
        self.assertEqual(updated["name"], "Alicia")    # REQ-04: name updated

        # Step 3: retrieve and confirm state
        record = self.registry.get_patient(pid)
        self.assertEqual(record["patient_id"], pid)    # REQ-03: ID still P-101
        self.assertEqual(record["name"], "Alicia")     # REQ-04: persisted name
        self.assertNotEqual(record["name"], "Alice")   # old name is gone

    def test_component_update_nonexistent_raises_key_error(self):
        """
        CT-02 - Failure workflow: update on unregistered ID is rejected.
        Workflow: update_patient_name() on unregistered ID -> KeyError raised,
                  get_patient() also raises KeyError (record was never inserted).
        TESTS: REQ-02, REQ-04
        Branch coverage: name guard False (valid name) -> ID guard True -> KeyError.
        Condition coverage: C1 (not isinstance) = False, C2 (name=="") = False,
        C3 (ID not in patients) = True.
        """
        # Step 1: update a patient ID that was never registered — must raise KeyError
        with self.assertRaises(KeyError):
            self.registry.update_patient_name("P-9999", "Ghost")

        # Step 2: confirm no ghost record was inserted
        with self.assertRaises(KeyError):
            self.registry.get_patient("P-9999")

    def test_component_register_delete_retrieve_fails(self):
        """
        CT-03 - Valid failure workflow.
        Workflow: register_patient() -> delete_patient() -> get_patient()
        TESTS: REQ-01, REQ-02, REQ-05
        Branch coverage: True path of `patient_id not in self.patients` in
        get_patient() after deletion — complementary to CT-01's False path.
        Condition coverage: C1 (not isdigit) = False, C2 (<101) = False,
        then missing-ID guard = True -> KeyError raised.
        """
        # Step 1: register
        pid = self.registry.register_patient("Bob")
        self.assertEqual(pid, "P-101")

        # Step 2: delete
        result = self.registry.delete_patient(pid)
        self.assertTrue(result)

        # Step 3: retrieve must now fail with KeyError
        with self.assertRaises(KeyError):
            self.registry.get_patient(pid)


if __name__ == '__main__':
    unittest.main()

# test_patient.py
# Unit tests for PatientRegistry class.
import unittest
from patient_registry import PatientRegistry


class TestPatientRegistry(unittest.TestCase):

    # Set up a new PatientRegistry instance before each test
    def setUp(self):
        self.registry = PatientRegistry()

    def test_register_retrieve(self):
        """Test registering a patient and retrieving their information."""
        # REQ-01: Register Patient
        pid = self.registry.register_patient('Bob')

        # REQ-02: Retrieve Patient Data
        record = self.registry.get_patient(pid)

        # Verify Data
        self.assertEqual(record['name'], 'Bob')
        self.assertEqual(record['patient_id'], 'P-101')
        self.assertEqual(pid, 'P-101')

    def test_search_for_non_existent_patient(self):
        """Test that searching for a non-existent patient raises KeyError."""
        # REQ-02: Non-existent patient raises KeyError
        # Use assertRaises
        with self.assertRaises(KeyError):
            self.registry.get_patient('P-9999')

    def test_register_invalid_name(self):
        """Test registering patient with invalid name raises ValueError."""
        # REQ-01: Empty name raises ValueError - Willhite
        with self.assertRaises(ValueError):
            self.registry.register_patient("")

    def test_invalid_patient_id_format(self):
        """Test retrieving with invalid patient ID raises ValueError."""
        # REQ-02: Invalid patient ID format raises ValueError - Willhite
        with self.assertRaises(ValueError):
            self.registry.get_patient("ABC")

    def test_get_patient_by_id(self):
        """Test retrieving a patient record using their Patient ID."""
        # REQ-03: The system shall allow retrieving a patient record
        # using their Patient ID. - Willhite
        test_name = "Charlie"
        pid = self.registry.register_patient(test_name)
        record = self.registry.get_patient(pid)

        self.assertEqual(record["name"], test_name)
        self.assertEqual(record["patient_id"], pid)
        self.assertEqual(pid, "P-101")

    def test_update_patient_name(self):
        """Test updating a patient's name using their Patient ID."""
        # REQ-04: Update a patient's name using Patient ID - Willhite
        pid = self.registry.register_patient("Alice")
        updated_record = self.registry.update_patient_name(pid, "Alicia")

        # Verify the return value
        self.assertEqual(updated_record["name"], "Alicia")
        self.assertEqual(updated_record["patient_id"], pid)

        # Verify the name was updated in storage
        retrieved_record = self.registry.get_patient(pid)
        self.assertEqual(retrieved_record["name"], "Alicia")
        self.assertEqual(pid, "P-101")

    def test_update_non_existent_patient(self):
        """Test that updating a non-existent patient raises KeyError."""
        # REQ-04: Updating non-existent patient raises KeyError
        with self.assertRaises(KeyError):
            self.registry.get_patient("P-9999")
            self.registry.update_patient_name("P-9999", "Nobody")

    def test_update_invalid_name(self):
        """Test updating patient with invalid name raises ValueError."""
        # REQ-04: Empty name raises ValueError - Willhite
        pid = self.registry.register_patient("Alice")
        with self.assertRaises(ValueError):
            self.registry.update_patient_name(pid, "")

    def test_delete_patient(self):
        """Test deleting a patient record using their Patient ID."""
        # REQ-05: Delete patient using Patient ID - Willhite
        pid = self.registry.register_patient("Bob")
        result = self.registry.delete_patient(pid)

        # Verify deletion returns True
        self.assertTrue(result)

        # Confirm patient is deleted
        with self.assertRaises(KeyError):
            self.registry.get_patient(pid)

    def test_delete_non_existent_patient(self):
        """Test that deleting a non-existent patient raises KeyError."""
        # REQ-05: Deleting non-existent patient raises KeyError
        with self.assertRaises(KeyError):
            self.registry.delete_patient("P-9999")


if __name__ == '__main__':
    unittest.main()

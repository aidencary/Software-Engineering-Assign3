import unittest
from patient_registry import PatientRegistry

class TestPatientRegistry(unittest.TestCase):
    
    def setUp(self):
        self.registry = PatientRegistry()

    def test_register_retrieve(self):
        # REQ-01: Register Patient
        pid = self.registry.register_patient('Bob')

        # REQ-02: Retrieve Patient Data
        record = self.registry.get_patient(pid)
        
        # Verify Data
        self.assertEqual(record['name'], 'Bob')
        self.assertEqual(pid, 'P-101')


        


    def test_search_for_non_existent_patient(self):
        # REQ-02: Non-existent patient raises KeyError
        # Use assertRaises
        with self.assertRaises(KeyError):
            self.registry.get_patient('P-9999')



    def test_register_invalid_name(self):
        # REQ-01: Empty name raises ValueError - Willhite
        with self.assertRaises(ValueError):
            self.registry.register_patient("")



    def test_invalid_patient_id_format(self):
        # REQ-02: Invalid patient ID format raises ValueError - Willhite
        with self.assertRaises(ValueError):
            self.registry.get_patient("ABC")

    """

    def test_get_patient_by_id(self):
    
    # REQ-03: The system shall allow retrieving a patient record using their Patient ID. - Willhite
    
        test_name = "Charlie"
        pid = self.registry.register_patient(test_name)
        record = self.registry.get_patient(pid)

        self.assertEqual(record["name"], test_name)
        self.assertEqual(record["patient_id"], pid)
    """




    """

    def test_update_patient_name(self):
    
         # REQ-04: Update a patient's name using Patient ID - Willhite
    
        pid = self.registry.register_patient("Alice")
        updated_record = self.registry.update_patient_name(pid, "Alicia")

        self.assertEqual(updated_record["name"], "Alicia")
        self.assertEqual(pid, "P-101")

    """
    
    """
    def test_update_non_existent_patient(self):
    
        #REQ-04: Updating a non-existent patient raises KeyError - Willhite
    
        with self.assertRaises(KeyError):
            self.registry.update_patient_name("P-9999", "Nobody")

    """

    """
    def test_delete_patient(self):
    
        # REQ-05: Delete patient using Patient ID - Willhite
    
        pid = self.registry.register_patient("Bob")
        result = self.registry.delete_patient(pid)

        self.assertTrue(result)

        # Confirm patient is deleted
        with self.assertRaises(KeyError):
            self.registry.get_patient(pid)

    """

    """

    def test_delete_non_existent_patient(self):
    
        # REQ-05: Deleting non-existent patient raises KeyError - Willhite
    
        with self.assertRaises(KeyError):
            self.registry.delete_patient("P-9999")
             

     """     



if __name__ == '__main__':
    unittest.main()
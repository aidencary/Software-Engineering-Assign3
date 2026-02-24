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
        # REQ-01: Empty name raises ValueError
        with self.assertRaises(ValueError):
            self.registry.register_patient("")


    def test_invalid_patient_id_format(self):
        # REQ-02: Invalid patient ID format raises ValueError
        with self.assertRaises(ValueError):
            self.registry.get_patient("ABC")


            
if __name__ == '__main__':
    unittest.main()
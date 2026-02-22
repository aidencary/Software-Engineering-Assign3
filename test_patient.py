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
        # Use assertRaises
        with self.assertRaises(KeyError):
            self.registry.get_patient('P-9999')
            
if __name__ == '__main__':
    unittest.main()
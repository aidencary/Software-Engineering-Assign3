import unittest
from patient_registry import PatientRegistry

class TestPatientRegistry(unittest.TestCase):
    
    def setUp(self):
        self.registry = PatientRegistry()

    def test_register_patient(self):
        """
        Test cases for register_patient(self, name: str) method.
        TESTS: REQ-01
        """
        print('\nTesting register_patient()...\n')

        if self.registry.patients:
            self.registry.patients.clear()

        tests = [('First Patient', 'Alice', 'P-101'),
                 ('Second Patient', 'Bob', 'P-102'),
                 ('Non-String Input', 42, ValueError),
                 ('Empty String', '', ValueError)]
        for test_name, patient_name, expected in tests:
            try:
                actual = self.registry.register_patient(patient_name)
            except ValueError as e:
                actual = type(e)

            if actual == expected:
                print(f'{test_name}: PASS')
            else:
                print(f'{test_name}: FAIL (Expected {expected}, Got {actual})')


    def test_get_patient(self):
        """
        Test cases for get_patient(self, patient_id: str) method.
        TESTS: REQ-02
        """
        print('\nTesting get_patient()...\n')

        if self.registry.patients:
            self.registry.patients.clear()
            
        self.registry.register_patient('Alice')

        tests = [('Normal Input', 'P-101', 'Alice'),
                 ('ID Out of Bounds', 'P-99', ValueError),
                 ('Wrong Format 1', 101, KeyError),
                 ('Wrong Format 2', 'P-Bob', ValueError),
                 ('Non-Existent ID', 'P-999', KeyError)]
        
        for test_name, pid, expected in tests:
            try:
                actual = self.registry.get_patient(pid)['name']
            except (ValueError, KeyError) as e:
                actual = type(e)
            
            if actual == expected:
                print(f'{test_name}: PASS')
            else:
                print(f'{test_name}: FAIL (Expected {expected}, Got {actual})')


    def test_update_patient_name(self):
        """
        Test cases for update_patient_name(self, patient_id, name) method.
        TESTS: REQ-04
        """
        print('\nTesting update_patient_name()...\n')

        if self.registry.patients:
            self.registry.patients.clear()

        self.registry.register_patient('Alice')

        tests = [('Normal', 'Bob', 'Bob'),
                 ('Non-String Input', 42, ValueError),
                 ('Empty String', '', ValueError)]
        
        for test_name, patient_name, expected in tests:
            try:
                self.registry.update_patient_name('P-101', patient_name)
                actual = self.registry.get_patient('P-101')['name']
            except ValueError as e:
                actual = type(e)

            if actual == expected:
                print(f'{test_name}: PASS')
            else:
                print(f'{test_name}: FAIL (Expected {expected}, Got {actual})')


    def test_delete_patient(self):
        """
        Test cases for delete_patient(self, patient_id) method.
        TESTS: REQ-05
        """
        print('\nTesting delete_patient()...\n')

        tests = [('Normal', 'P-101', KeyError)]
        
        for test_name, pid, expected in tests:
            if self.registry.patients:
                self.registry.patients.clear()

            self.registry.register_patient('Alice')

            try:
                self.registry.delete_patient(pid)
                self.registry.get_patient(pid)
            except (ValueError, KeyError) as e:
                actual = type(e)

            if actual == expected:
                print(f'{test_name}: PASS')
            else:
                print(f'{test_name}: FAIL (Expected {expected}, Got {actual})')


if __name__ == '__main__':
    unittest.main()
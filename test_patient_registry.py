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

        self.registry = PatientRegistry()

        # Test cases: normal input, non-string input, empty string
        tests = [('First Patient', 'Alice', 'P-101'),
                 ('Second Patient', 'Bob', 'P-102'),
                 ('Non-String Input', 42, ValueError),
                 ('Empty String', '', ValueError)]
        
        # Loop through test cases and verify results
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

        self.registry = PatientRegistry()
        
        # Register a patient for testing
        self.registry.register_patient('Alice')

        # Test cases: normal input, ID out of bounds, wrong format, non-existent ID
        tests = [('Normal Input', 'P-101', 'Alice'),
                 ('ID Out of Bounds', 'P-99', ValueError),
                 ('Wrong Format 1', 101, KeyError),
                 ('Wrong Format 2', 'P-Bob', ValueError),
                 ('Non-Existent ID', 'P-999', KeyError)]
        
        # Loop through test cases and verify results
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

        self.registry = PatientRegistry()

        # Register a patient for testing
        self.registry.register_patient('Alice')

        # Test cases: normal input, non-string input, empty string
        tests = [('Normal', 'Bob', 'Bob'),
                 ('Non-String Input', 42, ValueError),
                 ('Empty String', '', ValueError)]
        
        # Loop through test cases and verify results
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

        # Test cases: normal deletion, non-existent ID
        tests = [('Normal', 'P-101', KeyError),
                 ('Non-Existent ID', 'P-999', KeyError)]
        
        # Loop through test cases and verify results
        for test_name, pid, expected in tests:
            self.registry = PatientRegistry()

            self.registry.register_patient('Alice')

            try:
                self.registry.delete_patient(pid)
                self.registry.get_patient(pid)
            except (KeyError) as e:
                actual = type(e)

            if actual == expected:
                print(f'{test_name}: PASS')
            else:
                print(f'{test_name}: FAIL (Expected {expected}, Got {actual})')


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
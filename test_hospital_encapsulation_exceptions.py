import unittest
from datetime import date
from hospital_encapsulation_exceptions import Patient, Department, InvalidAgeError, InvalidDepartmentError

class TestHospital(unittest.TestCase):
    def test_patient_creation(self):
        patient = Patient(1, "Alice", 30, date(2023, 5, 1))
        self.assertEqual(patient.patient_id, 1)
        self.assertEqual(patient.age, 30)

    def test_invalid_age(self):
        with self.assertRaises(InvalidAgeError):
            Patient(2, "Bob", 130, date(2023, 5, 1))

    def test_empty_name(self):
        with self.assertRaises(ValueError) as context:
            Patient(3, "", 25, date(2023, 5, 1))
        self.assertEqual(str(context.exception), "Name cannot be empty.")

    def test_department_add_patient(self):
        dept = Department("Cardiology")
        patient = Patient(4, "Charlie", 40, date(2022, 3, 15))
        dept.add_patient(patient)
        self.assertIn(str(patient), str(dept))

    def test_invalid_remove_patient(self):
        dept = Department("Neurology")
        patient = Patient(5, "Diana", 35, date(2023, 1, 10))
        dept.add_patient(patient)
        with self.assertRaises(InvalidDepartmentError):
            dept.remove_patient(999)

if __name__ == "__main__":
    unittest.main()

# test_hospital.py

import unittest
from hospital import Patient, AdultPatient, ChildPatient

class TestHospitalInheritance(unittest.TestCase):

    def test_adult_patient(self):
        patient = AdultPatient(1, "John Doe", 45, "Flu")
        self.assertEqual(patient.get_info(),
                         "Patient ID: 1, Name: John Doe, Age: 45, Condition: Flu, Chronic Conditions: None")
        patient.add_chronic_condition("Hypertension")
        self.assertIn("Hypertension", patient.chronic_conditions)

    def test_child_patient(self):
        patient = ChildPatient(2, "Jane Doe", 10, "Cold")
        self.assertEqual(patient.get_info(),
                         "Patient ID: 2, Name: Jane Doe, Age: 10, Condition: Cold, Vaccinations: None")
        patient.add_vaccination("Polio")
        self.assertIn("Polio", patient.vaccinations)

    def test_polymorphism(self):
        patients = [
            AdultPatient(1, "John Doe", 45, "Flu"),
            ChildPatient(2, "Jane Doe", 10, "Cold")
        ]
        self.assertTrue(all(isinstance(p.get_info(), str) for p in patients))

if __name__ == "__main__":
    unittest.main()

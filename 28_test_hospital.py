import unittest
from hospital_entities import Patient, Ward
from hospital_database import HospitalDatabase


class TestHospitalDatabase(unittest.TestCase):
    def test_patient_management(self):
        db = HospitalDatabase()
        patient = Patient("P001", "Алиса Босканович", 30, "Грипп")
        db.add_patient(patient)
        self.assertEqual(db.get_patient("P001").name, "Алиса Босканович")
        db.delete_patient("P001")
        self.assertIsNone(db.get_patient("P001"))

    def test_ward_management(self):
        db = HospitalDatabase()
        ward = Ward("W001", 2)
        db.add_ward(ward)
        self.assertEqual(db.get_ward("W001").capacity, 2)
        db.delete_ward("W001")
        self.assertIsNone(db.get_ward("W001"))

    def test_assign_patient_to_ward(self):
        ward = Ward("W001", 2)
        patient = Patient("P001", "Алиса Босканович", 30, "Flu")
        ward.add_patient(patient)
        self.assertIn(patient, ward.patients)


if __name__ == "__main__":
    unittest.main()

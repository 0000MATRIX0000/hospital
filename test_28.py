import unittest
from hospital_entities import Patient, Doctor, Ward  # Импорт классов из hospital_entities
from hospital_database import HospitalDatabase  # Импорт класса из hospital_database

class TestHospital(unittest.TestCase):

    def setUp(self):
        """Создаем необходимые объекты для тестов."""
        self.patient = Patient("001", "Иванов", 30, "ОРВИ")
        self.doctor = Doctor("D001", "Смирнов", "Терапевт")
        self.ward = Ward("W001", 2)
        self.database = HospitalDatabase()

    def test_add_patient(self):
        """Тестируем добавление пациента в базу данных."""
        self.database.add_patient(self.patient)
        self.assertEqual(len(self.database.patients), 1)
        self.assertEqual(self.database.get_patient("001"), self.patient)

    def test_assign_patient_to_ward(self):
        """Тестируем назначение пациента в палату."""
        self.database.add_patient(self.patient)
        self.database.add_ward(self.ward)
        self.ward.add_patient(self.patient)
        self.assertIn(self.patient, self.ward.patients)

if __name__ == '__main__':
    unittest.main()

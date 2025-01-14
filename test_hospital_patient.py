import unittest
from hospital_patient import HospitalPatient, PersistenceAccount
from unittest.mock import patch

class TestHospitalPatient(unittest.TestCase):

    def setUp(self):
        # Создаем нового пациента для тестов
        self.patient = HospitalPatient("Popov Alex", 30, "Pneumonia")

    def test_initialization(self):
        self.assertEqual(self.patient.name, "Popov Alex")
        self.assertEqual(self.patient.age, 30)
        self.assertEqual(self.patient.diagnosis, "Pneumonia")
        self.assertEqual(self.patient.patient_id, 1)
        self.assertEqual(len(self.patient.history), 1)  # Должна быть одна транзакция - admission

    def test_add_transaction(self):
        self.patient.add_transaction("Started treatment")
        self.assertEqual(len(self.patient.history), 2)  # Ожидается 2 транзакции

    def test_discharge(self):
        self.patient.discharge()
        self.assertTrue(self.patient.is_discharge)
        self.assertIn('Discharge', [t['operation'] for t in self.patient.history])

    def test_persistence(self):
        # Тестируем сериализацию и десериализацию
        PersistenceAccount.serialize(self.patient)
        restored_patient = PersistenceAccount.deserialize()
        self.assertEqual(restored_patient.name, self.patient.name)
        self.assertEqual(restored_patient.age, self.patient.age)
        self.assertEqual(restored_patient.diagnosis, self.patient.diagnosis)
        self.assertEqual(restored_patient.patient_id, self.patient.patient_id)

    def test_destruction(self):
        # Патчируем print, чтобы проверить вызов деструктора
        with patch('builtins.print') as mocked_print:
            del self.patient  # Удаляем пациента, вызывается деструктор
            mocked_print.assert_called_with("Patient 1 (Popov Alexpython) is being removed from memory.")

if __name__ == "__main__":
    unittest.main()

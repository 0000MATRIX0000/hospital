import pickle
from datetime import datetime

class HospitalPatient:
    _id_counter = 0

    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.patient_id = HospitalPatient._get_next_id()
        self.history = []
        self.is_discharge = False
        self.add_transaction('Admission')

    @classmethod
    def _get_next_id(cls):
        cls._id_counter += 1
        return cls._id_counter

    def add_transaction(self, operation):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaction = {
            'operation': operation,
            'timestamp': timestamp,
            'patient_id': self.patient_id
        }
        self.history.append(transaction)

    def discharge(self):
        self.is_discharge = True
        self.add_transaction('Discharge')

    def __del__(self):
        # Clean-up actions, for example, logging the patient's discharge or writing history to a file
        print(f"Patient {self.patient_id} ({self.name}) is being removed from memory.")
        self.add_transaction('Destruction')

    def __str__(self):
        return f"Patient {self.patient_id}: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}"

    def get_transaction(self):
        return self.history


# Сериализация (Persistence)
class PersistenceAccount:
    @staticmethod
    def serialize(patient):
        with open('patient_data.pkl', 'wb') as f:
            pickle.dump(patient, f)

    @staticmethod
    def deserialize():
        with open('patient_data.pkl', 'rb') as f:
            patient = pickle.load(f)
        return patient

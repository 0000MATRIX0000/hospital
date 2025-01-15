from hospital_entities import Patient, Doctor, Ward


class HospitalDatabase:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.wards = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    def add_ward(self, ward):
        self.wards[ward.ward_id] = ward

    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

    def get_doctor(self, doctor_id):
        return self.doctors.get(doctor_id)

    def get_ward(self, ward_id):
        return self.wards.get(ward_id)

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]

    def delete_doctor(self, doctor_id):
        if doctor_id in self.doctors:
            del self.doctors[doctor_id]

    def delete_ward(self, ward_id):
        if ward_id in self.wards:
            del self.wards[ward_id]

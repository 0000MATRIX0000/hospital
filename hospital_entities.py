class Patient:
    def __init__(self, patient_id, name, age, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Condition: {self.condition}"


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}"


class Ward:
    def __init__(self, ward_id, capacity):
        self.ward_id = ward_id
        self.capacity = capacity
        self.patients = []

    def add_patient(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
        else:
            raise ValueError("Ward is full")

    def remove_patient(self, patient_id):
        self.patients = [p for p in self.patients if p.patient_id != patient_id]

    def __str__(self):
        patients_info = "\n  ".join(str(p) for p in self.patients) if self.patients else "No patients"
        return f"Ward ID: {self.ward_id}, Capacity: {self.capacity}, Patients:\n  {patients_info}"

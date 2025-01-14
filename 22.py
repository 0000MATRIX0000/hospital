from datetime import date

_next_hospital_id = 0

def _generate_hospital_id():
    global _next_hospital_id
    _next_hospital_id += 1
    return _next_hospital_id

class Hospital:
    def __init__(self, name="Unknown", location="Unknown", capacity=0):
        self._id = _generate_hospital_id()
        self.name = name
        self.location = location
        self.capacity = capacity
        self.current_patients = 0
        self.established_date = date.today()

    def admit_patient(self):
        if self.current_patients < self.capacity:
            self.current_patients += 1
        else:
            raise ValueError("Hospital is at full capacity!")

    def discharge_patient(self):
        if self.current_patients > 0:
            self.current_patients -= 1
        else:
            raise ValueError("No patients to discharge!")

    def __str__(self):
        return (
            f"Hospital ID: {self._id}, Name: {self.name}, Location: {self.location}, "
            f"Capacity: {self.capacity}, Current Patients: {self.current_patients}, "
            f"Established Date: {self.established_date}"
        )

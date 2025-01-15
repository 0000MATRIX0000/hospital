# hospital.py

class Patient:
    def __init__(self, patient_id, name, age, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    def get_info(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Condition: {self.condition}"

    def update_condition(self, new_condition):
        self.condition = new_condition
        return f"Condition updated to: {self.condition}"

class AdultPatient(Patient):
    def __init__(self, patient_id, name, age, condition, chronic_conditions=None):
        super().__init__(patient_id, name, age, condition)
        self.chronic_conditions = chronic_conditions or []

    def add_chronic_condition(self, condition):
        self.chronic_conditions.append(condition)
        return f"Added chronic condition: {condition}"

    def get_info(self):
        chronic = ", ".join(self.chronic_conditions) if self.chronic_conditions else "None"
        return f"{super().get_info()}, Chronic Conditions: {chronic}"

class ChildPatient(Patient):
    def __init__(self, patient_id, name, age, condition, vaccinations=None):
        super().__init__(patient_id, name, age, condition)
        self.vaccinations = vaccinations or []

    def add_vaccination(self, vaccine):
        self.vaccinations.append(vaccine)
        return f"Vaccination added: {vaccine}"

    def get_info(self):
        vaccines = ", ".join(self.vaccinations) if self.vaccinations else "None"
        return f"{super().get_info()}, Vaccinations: {vaccines}"

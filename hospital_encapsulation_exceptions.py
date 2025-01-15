class InvalidAgeError(Exception):
    """Исключение для недопустимого возраста пациента."""
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Invalid age: {self.age}. Age must be between 0 and 120."

class InvalidDepartmentError(Exception):
    """Исключение для недопустимого отдела в больнице."""
    def __init__(self, department):
        self.department = department

    def __str__(self):
        return f"Invalid department: {self.department}. Department not found."

class Patient:
    def __init__(self, patient_id, name, age, date_of_registration):
        self.__patient_id = patient_id
        self.name = name  # Инициализация через сеттер
        self.age = age
        self.date_of_registration = date_of_registration

    @property
    def patient_id(self):
        return self.__patient_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():  # Проверка на пустую строку
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 120):
            raise InvalidAgeError(value)
        self.__age = value

    def __str__(self):
        return f"Patient ID: {self.__patient_id}, Name: {self.__name}, Age: {self.__age}, Registered on: {self.date_of_registration}"

class Department:
    def __init__(self, department_name):
        self.__department_name = department_name  # Приватный атрибут
        self.__patients = []  # Список пациентов

    @property
    def department_name(self):
        return self.__department_name

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient instances can be added.")
        self.__patients.append(patient)

    def remove_patient(self, patient_id):
        for patient in self.__patients:
            if patient.patient_id == patient_id:
                self.__patients.remove(patient)
                return
        raise InvalidDepartmentError(patient_id)

    def __str__(self):
        return f"Department: {self.__department_name}, Patients: {[str(p) for p in self.__patients]}"

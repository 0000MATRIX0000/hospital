class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_info(self):
        return {
            "name": self.name,
            "location": self.location,
            "departments": [dept.name for dept in self.departments]
        }

class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_info(self):
        return {
            "name": self.name,
            "doctors": [doctor.get_info() for doctor in self.doctors]
        }

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def get_info(self):
        return {
            "name": self.name,
            "specialization": self.specialization
        }

if __name__ == '__main__':
    # Создаем больницу
    hospital = Hospital("City Hospital", "123 Main St")

    # Создаем отделения
    cardiology = Department("Cardiology")
    neurology = Department("Neurology")

    # Добавляем отделения в больницу
    hospital.add_department(cardiology)
    hospital.add_department(neurology)

    # Создаем докторов
    doctor1 = Doctor("Dr.Ivanov", "Cardiologist")
    doctor2 = Doctor("Dr. Popov", "Neurologist")

    # Добавляем докторов в отделения
    cardiology.add_doctor(doctor1)
    neurology.add_doctor(doctor2)

    # Проверяем данные больницы
    hospital_info = hospital.get_info()
    print("Hospital Information:", hospital_info)

    # Проверяем данные отделений
    for department in hospital.departments:
        print("Department Information:", department.get_info())

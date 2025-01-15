from hospital_entities import Patient, Doctor, Ward
from hospital_database import HospitalDatabase


class HospitalTerminal:
    def __init__(self):
        self.database = HospitalDatabase()

    def run(self):
        while True:
            print("\n--- Система управления больницей ---")
            print("1. Добавить пациента")
            print("2. Добавить врача")
            print("3. Добавить палату")
            print("4. Просмотреть пациентов")
            print("5. Просмотреть врачей")
            print("6. Просмотреть палаты")
            print("7. Назначить пациента в палату")
            print("8. Удалить пациента")
            print("9. Выход")
            choice = int(input("Выберите опцию: "))

            if choice == 1:
                self.add_patient()
            elif choice == 2:
                self.add_doctor()
            elif choice == 3:
                self.add_ward()
            elif choice == 4:
                self.view_patients()
            elif choice == 5:
                self.view_doctors()
            elif choice == 6:
                self.view_wards()
            elif choice == 7:
                self.assign_patient_to_ward()
            elif choice == 8:
                self.assign_patient_to_ward()
            elif choice == 9:
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def add_patient(self):
        patient_id = input("Введите ID пациента: ")
        name = input("Введите имя пациента: ")
        age = int(input("Введите возраст пациента: "))
        condition = input("Введите диагноз пациента: ")
        patient = Patient(patient_id, name, age, condition)
        self.database.add_patient(patient)
        print("Пациент успешно добавлен.")

    def add_doctor(self):
        doctor_id = input("Введите ID врача: ")
        name = input("Введите имя врача: ")
        specialization = input("Введите специализацию врача: ")
        doctor = Doctor(doctor_id, name, specialization)
        self.database.add_doctor(doctor)
        print("Врач успешно добавлен.")

    def add_ward(self):
        ward_id = input("Введите ID палаты: ")
        capacity = int(input("Введите вместимость палаты: "))
        ward = Ward(ward_id, capacity)
        self.database.add_ward(ward)
        print("Палата успешно добавлена.")

    def view_patients(self):
        if not self.database.patients:
            print("Список пациентов пуст.")
        for patient in self.database.patients.values():
            print(patient)

    def view_doctors(self):
        if not self.database.doctors:
            print("Список врачей пуст.")
        for doctor in self.database.doctors.values():
            print(doctor)

    def view_wards(self):
        if not self.database.wards:
            print("Список палат пуст.")
        for ward in self.database.wards.values():
            print(ward)

    def assign_patient_to_ward(self):
        patient_id = input("Введите ID пациента: ")
        ward_id = input("Введите ID палаты: ")

        patient = self.database.get_patient(patient_id)
        ward = self.database.get_ward(ward_id)

        if not patient:
            print("Пациент не найден.")
            return
        if not ward:
            print("Палата не найдена.")
            return

        try:
            ward.add_patient(patient)
            print("Пациент успешно назначен в палату.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    HospitalTerminal().run()

class Patient:
    """
    Класс для хранения информации о пациенте.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Patient: {self.first_name} {self.last_name}, Age: {self.age}"

class Hospital:
    """
    Класс для управления больницей и списком пациентов.
    """
    def __init__(self):
        self.patients = []  # Список пациентов

    def add_patient(self, patient):
        """
        Метод для добавления пациента в больницу.
        """
        self.patients.append(patient)

    def list_patients(self):
        """
        Метод для вывода списка всех пациентов в больнице.
        """
        return [str(patient) for patient in self.patients]
import time

def log_execution_time(func):
    """
    Декоратор для измерения времени выполнения метода.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время начала
        result = func(*args, **kwargs)
        end_time = time.time()  # Засекаем время окончания
        print(f"Method {func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

def count_calls(func):
    """
    Декоратор для подсчёта числа вызовов метода.
    """
    def wrapper(*args, **kwargs):
        if not hasattr(func, 'calls'):
            func.calls = 0  # Инициализация счётчика
        func.calls += 1
        print(f"Method {func.__name__} called {func.calls} times")
        return func(*args, **kwargs)
    return wrapper


class Hospital:
    """
    Класс для управления больницей и списком пациентов.
    """
    def __init__(self):
        self.patients = []  # Список пациентов

    @log_execution_time
    @count_calls
    def add_patient(self, patient):
        """
        Метод для добавления пациента в больницу.
        """
        self.patients.append(patient)

    @log_execution_time
    @count_calls
    def list_patients(self):
        """
        Метод для вывода списка всех пациентов в больнице.
        """
        return [str(patient) for patient in self.patients]

# Создаём пациентов
patient1 = Patient("Anna", "M", 30)
patient2 = Patient("Alice", "P", 25)

# Создаём больницу
hospital = Hospital()

# Добавляем пациентов в больницу и выводим список пациентов
hospital.add_patient(patient1)
hospital.add_patient(patient2)

# Выводим список всех пациентов
print(hospital.list_patients())

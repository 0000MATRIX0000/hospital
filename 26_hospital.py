
import unittest


class Hospital:
    """
    Класс Hospital представляет больницу с её названием и вместимостью.
    """

    def __init__(self, name, capacity):
        """
        Инициализирует новый объект Hospital с названием и вместимостью.

        :param name: Название больницы
        :param capacity: Вместимость больницы
        """
        self.name = name
        self.capacity = capacity
        self.patients = []

    def add_patient(self, patient):
        """
        Добавляет пациента в список пациентов больницы.

        :param patient: Объект пациента, который добавляется в больницу.
        """
        self.patients.append(patient)

    def get_patients(self):
        """
        Возвращает список всех пациентов, находящихся в больнице.

        :return: Список пациентов
        """
        return self.patients

    def __str__(self):
        """
        Строковое представление объекта Hospital.

        :return: Название больницы
        """
        return f"Hospital: {self.name}"

    def __add__(self, other):
        """
        Перегрузка оператора + для добавления вместимости двух больниц.

        :param other: другая больница
        :return: новая больница с объединенной вместимостью
        """
        if isinstance(other, Hospital):
            return Hospital(f"{self.name} + {other.name}", self.capacity + other.capacity)
        return NotImplemented

    def __sub__(self, other):
        """
        Перегрузка оператора - для вычитания вместимости двух больниц.

        :param other: другая больница
        :return: новая больница с уменьшенной вместимостью
        """
        if isinstance(other, Hospital):
            return Hospital(f"{self.name} - {other.name}", self.capacity - other.capacity)
        return NotImplemented

    def __mul__(self, other):
        """
        Перегрузка оператора * для умножения вместимости больницы на число.

        :param other: число для умножения
        :return: новая больница с увеличенной вместимостью
        """
        if isinstance(other, (int, float)):
            return Hospital(f"{self.name} * {other}", self.capacity * other)
        return NotImplemented

    def __truediv__(self, other):
        """
        Перегрузка оператора / для деления вместимости больницы на число.

        :param other: число для деления
        :return: новая больница с уменьшенной вместимостью
        """
        if isinstance(other, (int, float)):
            return Hospital(f"{self.name} / {other}", self.capacity / other)
        return NotImplemented


class TestHospitalOperations(unittest.TestCase):

    def setUp(self):
        """
        Этот метод выполняется перед каждым тестом.
        Создаем два объекта Hospital для тестирования.
        """
        self.hospital1 = Hospital("Hospital A", 100)
        self.hospital2 = Hospital("Hospital B", 200)

    def test_addition(self):
        """
        Проверка перегрузки оператора + для объединения вместимости больниц.
        """
        new_hospital = self.hospital1 + self.hospital2
        self.assertEqual(new_hospital.capacity, 300)

    def test_subtraction(self):
        """
        Проверка перегрузки оператора - для вычитания вместимости больниц.
        """
        new_hospital = self.hospital1 - self.hospital2
        self.assertEqual(new_hospital.capacity, -100)

    def test_multiplication(self):
        """
        Проверка перегрузки оператора * для умножения вместимости больницы на число.
        """
        new_hospital = self.hospital1 * 2
        self.assertEqual(new_hospital.capacity, 200)

    def test_division(self):
        """
        Проверка перегрузки оператора / для деления вместимости больницы на число.
        """
        new_hospital = self.hospital2 / 2
        self.assertEqual(new_hospital.capacity, 100)


if __name__ == '__main__':
    unittest.main()

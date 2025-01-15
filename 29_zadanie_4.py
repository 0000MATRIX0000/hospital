import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget


class UnitConverter(QMainWindow):
    """
    Простое приложение для перевода значений из одних единиц измерения в другие.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Конвертер единиц")
        self.setFixedSize(300, 200)

        # Создание виджетов
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите значение")
        self.convert_button = QPushButton("Конвертировать")
        self.result_label_1 = QLabel("Результат 1: ")
        self.result_label_2 = QLabel("Результат 2: ")
        self.result_label_3 = QLabel("Результат 3: ")

        # Подключение кнопки
        self.convert_button.clicked.connect(self.convert_units)

        # Компоновка
        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.result_label_1)
        layout.addWidget(self.result_label_2)
        layout.addWidget(self.result_label_3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def convert_units(self):
        """
        Конвертация введённого значения в различные единицы.
        """
        try:
            value = float(self.input_field.text())
            self.result_label_1.setText(f"В килограммах: {value * 0.001} кг")
            self.result_label_2.setText(f"В граммах: {value} г")
            self.result_label_3.setText(f"В миллиграммах: {value * 1000} мг")
        except ValueError:
            self.result_label_1.setText("Ошибка: введите число.")
            self.result_label_2.clear()
            self.result_label_3.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UnitConverter()
    window.show()
    app.exec()

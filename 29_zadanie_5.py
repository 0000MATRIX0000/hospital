import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget


class Calculator(QMainWindow):
    """
    Простой калькулятор для выполнения арифметических выражений.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(300, 150)

        # Создание виджетов
        self.expression_field = QLineEdit(self)
        self.expression_field.setPlaceholderText("Введите выражение")
        self.calculate_button = QPushButton("Вычислить")
        self.result_field = QLineEdit(self)
        self.result_field.setReadOnly(True)

        # Подключение кнопки
        self.calculate_button.clicked.connect(self.calculate_expression)

        # Компоновка
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Введите выражение:"))
        layout.addWidget(self.expression_field)
        layout.addWidget(self.calculate_button)
        layout.addWidget(QLabel("Результат:"))
        layout.addWidget(self.result_field)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calculate_expression(self):
        """
        Вычисляет введённое арифметическое выражение.
        """
        try:
            expression = self.expression_field.text()
            result = eval(expression)
            self.result_field.setText(str(result))
        except Exception as e:
            self.result_field.setText("Ошибка")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    app.exec()

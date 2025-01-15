import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
from PySide6.QtCore import Qt


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 400)

        self.result_field = QLineEdit(self)  # Поле для отображения результата
        self.result_field.setAlignment(Qt.AlignRight)  # Выравнивание текста по правому краю
        self.result_field.setReadOnly(True)  # Сделаем поле только для чтения

        self.layout = QVBoxLayout()  # Главный вертикальный макет
        self.layout.addWidget(self.result_field)

        # Вспомогательные макеты
        self.buttons_layout = QVBoxLayout()

        # Добавим кнопки калькулятора
        self.create_buttons()

        self.layout.addLayout(self.buttons_layout)

        # Центральный виджет
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def create_buttons(self):
        """
        Создаём кнопки калькулятора.
        """
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]

        for row in buttons:
            row_layout = QHBoxLayout()
            for button in row:
                btn = QPushButton(button)
                btn.clicked.connect(self.on_button_click)
                row_layout.addWidget(btn)
            self.buttons_layout.addLayout(row_layout)

    def on_button_click(self):
        """
        Обработчик нажатий кнопок.
        """
        button_text = self.sender().text()

        if button_text == 'C':
            self.result_field.clear()  # Очистка поля
        elif button_text == '=':
            try:
                expression = self.result_field.text()
                result = str(eval(expression))  # Вычисление выражения
                self.result_field.setText(result)
            except Exception as e:
                self.result_field.setText('Ошибка')
        else:
            current_text = self.result_field.text()
            new_text = current_text + button_text
            self.result_field.setText(new_text)

    def keyPressEvent(self, event):
        """
        Перехватываем нажатие клавиш.
        """
        key = event.text()

        if key == 'C':
            self.result_field.clear()
        elif key == '=':
            try:
                expression = self.result_field.text()
                result = str(eval(expression))  # Вычисление выражения
                self.result_field.setText(result)
            except Exception as e:
                self.result_field.setText('Ошибка')
        elif key in '0123456789+-*/':
            current_text = self.result_field.text()
            new_text = current_text + key
            self.result_field.setText(new_text)

    def keyPressEvent(self, event):
        """
        Перехватываем нажатие клавиш.
        """
        key = event.text()

        if key == 'C':
            self.result_field.clear()
        elif key == '=':
            try:
                expression = self.result_field.text()
                result = str(eval(expression))  # Вычисление выражения
                self.result_field.setText(result)
            except Exception as e:
                self.result_field.setText('Ошибка')
        elif key in '0123456789+-*/':
            current_text = self.result_field.text()
            new_text = current_text + key
            self.result_field.setText(new_text)


# Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()  # Показываем окно
    sys.exit(app.exec())  # Запуск главного цикла приложения

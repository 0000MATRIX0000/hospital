from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QToolBar, QStatusBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("ToDo List")

        # Создаем главный виджет и устанавливаем его в качестве центрального
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Вертикальный макет для размещения элементов
        self.layout = QVBoxLayout(self.main_widget)
        self.task_input = QLineEdit(self)
        self.layout.addWidget(self.task_input)

        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        # Кнопка для добавления задачи
        self.add_button = QPushButton("Добавить задачу", self)
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        # Кнопка для удаления задачи
        self.remove_button = QPushButton("Удалить задачу", self)
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        # Кнопка для отметки задачи как выполненной
        self.mark_done_button = QPushButton("Отметить как выполненную", self)
        self.mark_done_button.clicked.connect(self.mark_done)
        self.layout.addWidget(self.mark_done_button)

        # Кнопка для отметки задачи как невыполненной
        self.mark_undone_button = QPushButton("Отметить как невыполненную", self)
        self.mark_undone_button.clicked.connect(self.mark_undone)
        self.layout.addWidget(self.mark_undone_button)

        # Панель инструментов
        self.toolbar = self.addToolBar("Toolbar")
        self.add_toolbar_actions()

        # Строка состояния
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()
            self.status_bar.showMessage(f"Задача '{task_text}' добавлена", 2000)

    def remove_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.status_bar.showMessage(f"Задача '{selected_item.text()}' удалена", 2000)
            self.task_list.takeItem(self.task_list.row(selected_item))

    def mark_done(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            selected_item.setForeground(Qt.green)
            self.status_bar.showMessage(f"Задача '{selected_item.text()}' выполнена", 2000)

    def mark_undone(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            selected_item.setForeground(Qt.black)
            self.status_bar.showMessage(f"Задача '{selected_item.text()}' не выполнена", 2000)

    def add_toolbar_actions(self):
        # Иконка для добавления задачи
        add_task_action = QAction(QIcon("D:/45/project/z.png"), "Добавить задачу", self)
        add_task_action.triggered.connect(self.add_task)
        self.toolbar.addAction(add_task_action)

        # Иконка для удаления задачи
        remove_task_action = QAction(QIcon("D:/45/project/o.png"), "Удалить задачу", self)
        remove_task_action.triggered.connect(self.remove_task)
        self.toolbar.addAction(remove_task_action)

        # Иконка для отметки задачи как выполненной
        mark_done_action = QAction(QIcon("D:/45/project/v.png"), "Отметить как выполненную", self)
        mark_done_action.triggered.connect(self.mark_done)
        self.toolbar.addAction(mark_done_action)

        # Иконка для отметки задачи как невыполненной
        mark_undone_action = QAction(QIcon("D:/45/project/d.png"), "Отметить как невыполненную", self)
        mark_undone_action.triggered.connect(self.mark_undone)
        self.toolbar.addAction(mark_undone_action)

        # Иконка для "О программе"
        about_action = QAction(QIcon("D:/45/project/pr.png"), "О программе", self)
        about_action.triggered.connect(self.show_about)
        self.toolbar.addAction(about_action)

    def show_about(self):
        about_message = """
        Приложение ToDo List
        Автор: Natali
        Версия: 1.0
        Дата создания: Январь 2025
        """
        self.status_bar.showMessage(about_message, 5000)

# Запуск приложения
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

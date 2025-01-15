from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QMenuBar, QToolBar, \
    QFileDialog, QDialog, QDialogButtonBox, QLineEdit, QMessageBox
from PySide6.QtGui import QIcon, QAction
import os
import shutil


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Manager")  # Устанавливаем заголовок окна
        self.setGeometry(200, 200, 800, 600)  # Задаем начальный размер и позицию окна

        # Инициализация интерфейса
        self.init_ui()

        # Хранилище для файлов
        self.storage_path = "D:/45/project/storage"  # Путь к хранилищу

        # Проверка существования хранилища, если нет - создание
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)  # Создаем директорию хранилища, если её нет

        # Список открытых файлов
        self.opened_files = {}

    def init_ui(self):
        # Создание меню и панели инструментов
        menu_bar = self.menuBar()  # Создаем меню
        file_menu = menu_bar.addMenu('File')  # Создаем пункт меню "File"

        # Панель инструментов
        toolbar = self.addToolBar("Main Toolbar")  # Добавляем панель инструментов
        toolbar.setMovable(True)  # Панель можно перемещать

        # Создание действий (QAction) с иконками для кнопок
        create_action = QAction(QIcon("D:/45/project/sa.png"), "Create New File",
                                self)  # Действие для создания нового файла
        create_action.triggered.connect(self.create_new_file)  # Подключаем действие к функции
        file_menu.addAction(create_action)  # Добавляем действие в меню
        toolbar.addAction(create_action)  # Добавляем действие на панель инструментов

        open_action = QAction(QIcon("D:/45/project/ot.png"), "Open File", self)  # Действие для открытия файла
        open_action.triggered.connect(self.open_file)  # Подключаем действие к функции
        file_menu.addAction(open_action)  # Добавляем действие в меню
        toolbar.addAction(open_action)  # Добавляем действие на панель инструментов

        save_action = QAction(QIcon("D:/45/project/oo.png"), "Save File", self)  # Действие для сохранения файла
        save_action.triggered.connect(self.save_file)  # Подключаем действие к функции
        file_menu.addAction(save_action)  # Добавляем действие в меню
        toolbar.addAction(save_action)  # Добавляем действие на панель инструментов

        close_action = QAction(QIcon("D:/45/project/za.png"), "Close Application",
                               self)  # Действие для закрытия приложения
        close_action.triggered.connect(self.close)  # Подключаем действие к функции
        file_menu.addAction(close_action)  # Добавляем действие в меню
        toolbar.addAction(close_action)  # Добавляем действие на панель инструментов

        delete_action = QAction(QIcon("D:/45/project/yd.png"), "Delete File", self)  # Действие для удаления файла
        delete_action.triggered.connect(self.delete_file)  # Подключаем действие к функции
        file_menu.addAction(delete_action)  # Добавляем действие в меню
        toolbar.addAction(delete_action)  # Добавляем действие на панель инструментов

        move_action = QAction(QIcon("D:/45/project/pe.png"), "Move Storage", self)  # Действие для перемещения хранилища
        move_action.triggered.connect(self.move_storage)  # Подключаем действие к функции
        file_menu.addAction(move_action)  # Добавляем действие в меню
        toolbar.addAction(move_action)  # Добавляем действие на панель инструментов

        info_action = QAction(QIcon("D:/45/project/ii.png"), "File Info",
                              self)  # Действие для отображения информации о файле
        info_action.triggered.connect(self.file_info)  # Подключаем действие к функции
        file_menu.addAction(info_action)  # Добавляем действие в меню
        toolbar.addAction(info_action)  # Добавляем действие на панель инструментов

        search_action = QAction(QIcon("D:/45/project/tt.png"), "Search Files", self)  # Действие для поиска файлов
        search_action.triggered.connect(self.search_files)  # Подключаем действие к функции
        file_menu.addAction(search_action)  # Добавляем действие в меню
        toolbar.addAction(search_action)  # Добавляем действие на панель инструментов

        settings_action = QAction(QIcon("D:/45/project/nn.png"), "Settings", self)  # Действие для настроек приложения
        settings_action.triggered.connect(self.settings)  # Подключаем действие к функции
        file_menu.addAction(settings_action)  # Добавляем действие в меню
        toolbar.addAction(settings_action)  # Добавляем действие на панель инструментов

        # Центральный виджет
        self.text_edit = QTextEdit(self)  # Создаем текстовое поле для редактирования
        self.setCentralWidget(self.text_edit)  # Устанавливаем его как центральный виджет

    def create_new_file(self):
        # Функция для создания нового файла
        file_name, _ = QFileDialog.getSaveFileName(self, "Create New File", self.storage_path,
                                                   "Text Files (*.txt);;Markdown Files (*.md)")  # Открываем диалоговое окно для сохранения файла
        if file_name:
            with open(file_name, 'w') as f:  # Открываем файл для записи
                f.write("")  # Создаем пустой файл
            self.open_file(file_name)  # Открываем созданный файл

    def open_file(self, file_name=None):
        # Функция для открытия файла
        if not file_name:  # Если имя файла не передано
            file_name, _ = QFileDialog.getOpenFileName(self, "Open File", self.storage_path,
                                                       "Text Files (*.txt);;Markdown Files (*.md)")  # Открываем диалоговое окно для выбора файла
        if file_name:  # Если файл выбран
            if file_name not in self.opened_files:  # Если файл ещё не открыт
                text_edit = QTextEdit(self)  # Создаем новое текстовое поле
                self.opened_files[file_name] = text_edit  # Сохраняем его в словарь открытых файлов
                text_edit.setText(open(file_name).read())  # Читаем содержимое файла и отображаем в текстовом поле
                self.setCentralWidget(text_edit)  # Устанавливаем его как центральный виджет

    def save_file(self):
        # Функция для сохранения файла
        current_file = self.get_current_file()  # Получаем имя текущего файла
        if current_file:
            with open(current_file, 'w') as f:  # Открываем файл для записи
                f.write(self.text_edit.toPlainText())  # Сохраняем текст из текстового поля в файл

    def get_current_file(self):
        # Функция для получения имени текущего файла
        for file_name, editor in self.opened_files.items():
            if editor == self.centralWidget():  # Если текстовое поле совпадает с текущим виджетом
                return file_name  # Возвращаем имя файла
        return None  # Если файл не найден, возвращаем None

    def delete_file(self):
        # Функция для удаления файла
        file_name = self.get_current_file()  # Получаем имя текущего файла
        if file_name and os.path.exists(file_name):  # Если файл существует
            confirm_dialog = QDialog(self)  # Создаем диалоговое окно для подтверждения удаления
            confirm_dialog.setWindowTitle("Confirm Deletion")  # Устанавливаем заголовок окна
            layout = QVBoxLayout(confirm_dialog)  # Создаем вертикальный лейаут
            confirm_dialog_input = QLineEdit(confirm_dialog)  # Создаем поле ввода для подтверждения
            confirm_dialog_input.setPlaceholderText("Type the name of the file to confirm deletion")  # Подсказка
            layout.addWidget(confirm_dialog_input)  # Добавляем поле ввода на форму
            confirm_dialog_buttons = QDialogButtonBox(
                QDialogButtonBox.Ok | QDialogButtonBox.Cancel)  # Кнопки для подтверждения
            layout.addWidget(confirm_dialog_buttons)  # Добавляем кнопки
            confirm_dialog_buttons.accepted.connect(
                lambda: self.confirm_deletion(file_name, confirm_dialog_input.text()))  # Подключаем обработку кнопки OK
            confirm_dialog_buttons.rejected.connect(confirm_dialog.reject)  # Подключаем обработку кнопки Cancel
            confirm_dialog.exec()  # Показываем диалог

    def confirm_deletion(self, file_name, input_text):
        # Функция для подтверждения удаления
        if input_text == os.path.basename(file_name):  # Если введенное имя совпадает с именем файла
            os.remove(file_name)  # Удаляем файл
            self.statusBar().showMessage(f"File {file_name} deleted successfully!")  # Показываем сообщение
            del self.opened_files[file_name]  # Удаляем файл из списка открытых файлов
        else:
            self.statusBar().showMessage("Deletion confirmation failed!")  # Если не совпало, показываем ошибку

    def move_storage(self):
        # Функция для перемещения хранилища
        new_location = QFileDialog.getExistingDirectory(self,
                                                        "Select New Directory for Storage")  # Открываем диалог для выбора нового пути
        if new_location:
            shutil.move(self.storage_path, new_location)  # Перемещаем хранилище в новую папку
            self.storage_path = new_location  # Обновляем путь хранилища
            self.statusBar().showMessage(f"Storage moved to {new_location}")  # Показываем сообщение о перемещении

    def file_info(self):
        # Функция для отображения информации о файле
        file_name = self.get_current_file()  # Получаем имя текущего файла
        if file_name:
            file_info = os.stat(file_name)  # Получаем информацию о файле
            QMessageBox.information(self, "File Info",
                                    f"File {file_name} was last modified on {file_info.st_mtime}")  # Отображаем дату последнего изменения файла

    def search_files(self):
        # Функция для поиска файлов
        search_term, _ = QFileDialog.getOpenFileName(self, "Search for Files",
                                                     self.storage_path)  # Открываем диалог для поиска файлов
        if search_term:
            found_files = [f for f in os.listdir(self.storage_path) if
                           search_term.lower() in f.lower()]  # Ищем файлы по запросу
            self.statusBar().showMessage(f"Found files: {', '.join(found_files)}")  # Показываем найденные файлы

    def settings(self):
        # Функция для настроек
        QMessageBox.information(self, "Settings", "Версия 1.0")  # Отображаем окно с настройками


app = QApplication([])  # Создаем приложение
window = MainWindow()  # Создаем главное окно
window.show()  # Отображаем окно
app.exec()  # Запускаем главный цикл приложения

import sys
import pandas as pd
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

# Путь к CSV-файлу для хранения данных о транзакциях
CSV_FILE = "transactions.csv"

# Проверяем, существует ли файл, если нет - создаём его с базовой структурой
if not pd.io.common.file_exists(CSV_FILE):
    pd.DataFrame(columns=["ID", "Дата", "Тип", "Сумма", "Баланс", "Комментарий"]).to_csv(CSV_FILE, index=False)

# Определение кастомной модели для работы с таблицей
class PandasTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    # Возвращает количество строк в таблице
    def rowCount(self, index):
        return len(self._data)

    # Возвращает количество колонок в таблице
    def columnCount(self, index):
        return len(self._data.columns)

    # Возвращает данные для отображения или редактирования в таблице
    def data(self, index, role):
        if not index.isValid():
            return None

        value = self._data.iloc[index.row(), index.column()]

        if role == Qt.DisplayRole or role == Qt.EditRole:
            return str(value)

        # Условное форматирование: выделение доходов и расходов цветом
        if role == Qt.BackgroundRole:
            if self._data.iloc[index.row(), 2] == "Доход":
                return QtGui.QBrush(QtGui.QColor("lightgreen"))
            elif self._data.iloc[index.row(), 2] == "Расход":
                return QtGui.QBrush(QtGui.QColor("lightcoral"))

        return None

    # Обновляет данные в модели при редактировании
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data.iloc[index.row(), index.column()] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True
        return False

    # Устанавливает флаги для редактирования ячеек
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    # Добавляет новую строку в таблицу
    def addRow(self, row_data):
        self.beginInsertRows(QtCore.QModelIndex(), len(self._data), len(self._data))
        self._data.loc[len(self._data)] = row_data
        self.endInsertRows()

    # Удаляет строку из таблицы
    def removeRow(self, row):
        self.beginRemoveRows(QtCore.QModelIndex(), row, row)
        self._data = self._data.drop(self._data.index[row]).reset_index(drop=True)
        self.endRemoveRows()

    # Сохраняет данные модели в CSV-файл
    def saveToFile(self):
        self._data.to_csv(CSV_FILE, index=False)

# Главное окно приложения
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Трекер финансов")
        self.resize(800, 600)

        # Загрузка данных из CSV-файла
        self.data = pd.read_csv(CSV_FILE)
        self.model = PandasTableModel(self.data)

        # Центральный виджет с таблицей
        self.table_view = QtWidgets.QTableView()
        self.table_view.setModel(self.model)
        self.setCentralWidget(self.table_view)

        # Боковое меню для навигации
        self.sidebar = QtWidgets.QDockWidget("Меню", self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)

        self.sidebar_menu = QtWidgets.QListWidget()
        self.sidebar_menu.addItems(["Управление транзакциями", "О приложении"])
        self.sidebar_menu.currentRowChanged.connect(self.switch_section)
        self.sidebar.setWidget(self.sidebar_menu)

        # Формы и кнопки для добавления/удаления транзакций
        self.form_widget = QtWidgets.QWidget()
        self.form_layout = QtWidgets.QFormLayout(self.form_widget)

        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())

        self.type_input = QtWidgets.QComboBox()
        self.type_input.addItems(["Доход", "Расход"])

        self.amount_input = QtWidgets.QLineEdit()
        self.comment_input = QtWidgets.QLineEdit()

        self.add_button = QtWidgets.QPushButton("Добавить транзакцию")
        self.add_button.clicked.connect(self.add_transaction)

        self.delete_button = QtWidgets.QPushButton("Удалить выбранные")
        self.delete_button.clicked.connect(self.delete_transaction)

        self.form_layout.addRow("Дата:", self.date_input)
        self.form_layout.addRow("Тип:", self.type_input)
        self.form_layout.addRow("Сумма:", self.amount_input)
        self.form_layout.addRow("Комментарий:", self.comment_input)
        self.form_layout.addRow(self.add_button)
        self.form_layout.addRow(self.delete_button)

        self.sidebar.setWidget(self.form_widget)

    # Переключение между разделами меню
    def switch_section(self, index):
        if index == 0:
            self.table_view.show()
        elif index == 1:
            QtWidgets.QMessageBox.information(self, "О приложении", "Трекер финансов\nВерсия 1.0")

    # Добавление новой транзакции в таблицу
    def add_transaction(self):
        try:
            new_id = len(self.data) + 1
            date = self.date_input.date().toString("yyyy-MM-dd")
            t_type = self.type_input.currentText()
            amount = float(self.amount_input.text())
            comment = self.comment_input.text()
            balance = self.data["Баланс"].iloc[-1] + (amount if t_type == "Доход" else -amount) if not self.data.empty else amount

            new_row = [new_id, date, t_type, amount, balance, comment]
            self.model.addRow(new_row)
            self.model.saveToFile()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", str(e))

    # Удаление выбранных строк из таблицы
    def delete_transaction(self):
        selected_indexes = self.table_view.selectionModel().selectedRows()
        for index in sorted(selected_indexes, reverse=True):
            self.model.removeRow(index.row())
        self.model.saveToFile()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

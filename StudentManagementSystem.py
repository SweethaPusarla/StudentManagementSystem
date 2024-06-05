import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QMessageBox, QLabel,
    QLineEdit, QHBoxLayout, QVBoxLayout, QDialog, QWidget, QPushButton,
    QTableWidgetItem, QTableWidget, QComboBox, QGridLayout
)
import mysql.connector

class DBHelper:
    def _init_(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2003",
            database="StudentManagementSystem"
        )
        self.c = self.conn.cursor()

    def add_student(self, sid, sname, dept, year, course_a, course_b, course_c):
        try:
            self.c.execute(
                "INSERT INTO student(sid, Sname, dept, year, course_a, course_b, course_c) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (sid, sname, dept, year, course_a, course_b, course_c)
            )
            self.conn.commit()
            QMessageBox.information(None, 'Successful', 'Student is added successfully to the database.')
        except Exception as e:
            QMessageBox.warning(None, 'Error', f'Could not add student to the database.\n{str(e)}')

    def search_student(self, sid):
        self.c.execute("SELECT * FROM student WHERE sid=%s", (sid,))
        data = self.c.fetchone()

        if not data:
            QMessageBox.warning(None, 'Error', f'Could not find any student with roll no {sid}')
            return None
        show_student(data)

    def delete_record(self, sid):
        try:
            self.c.execute("DELETE FROM student WHERE sid=%s", (sid,))
            self.conn.commit()
            QMessageBox.information(None, 'Successful', 'Student is deleted from the database.')
        except Exception as e:
            QMessageBox.warning(None, 'Error', f'Could not delete student from the database.\n{str(e)}')

    def _del_(self):
        self.conn.close()

def show_student(data):
    sid, sname, dept, year, course_a, course_b, course_c = data

    dept_map = [
        "Mechanical Engineering", "Chemical Engineering", "Software Engineering",
        "Biotech Engineering", "Computer Science and Engineering", "Information Technology"
    ]
    year_map = ["1st", "2nd", "3rd", "4th"]
    course_map = [
        "DBMS", "OS", "CN", "C++", "JAVA", "PYTHON", "THERMO", "MACHINE",
        "CELLS", "DS", "CRE", "MICROBES", "FERTILIZER", "PLANTS", "MOBILE APP"
    ]

    dept_name = dept_map[dept] if dept < len(dept_map) else "Unknown"
    year_name = year_map[year] if year < len(year_map) else "Unknown"
    course_a_name = course_map[course_a] if course_a < len(course_map) else "Unknown"
    course_b_name = course_map[course_b] if course_b < len(course_map) else "Unknown"
    course_c_name = course_map[course_c] if course_c < len(course_map) else "Unknown"

    table = QTableWidget()
    table.setWindowTitle("Student Details")
    table.setRowCount(7)
    table.setColumnCount(2)
    table.setHorizontalHeaderLabels(["Field", "Value"])

    fields = [
        ("Roll", str(sid)),
        ("Name", sname),
        ("Department", dept_name),
        ("Year", year_name),
        ("Slot A", course_a_name),
        ("Slot B", course_b_name),
        ("Slot C", course_c_name)
    ]

    for i, (field, value) in enumerate(fields):
        table.setItem(i, 0, QTableWidgetItem(field))
        table.setItem(i, 1, QTableWidgetItem(value))

    table.horizontalHeader().setStretchLastSection(True)

    dialog = QDialog()
    dialog.setWindowTitle("Student Details")
    dialog.resize(500, 300)
    layout = QVBoxLayout()
    layout.addWidget(table)
    dialog.setLayout(layout)
    dialog.exec()

class AddStudent(QDialog):
    def _init_(self):
        super()._init_()

        self.dept = -1
        self.year = -1
        self.sid = -1
        self.sname = ""
        self.course_a = -1
        self.course_b = -1
        self.course_c = -1

        self.btnCancel = QPushButton("Cancel", self)
        self.btnReset = QPushButton("Reset", self)
        self.btnAdd = QPushButton("Add", self)

        self.btnCancel.setFixedHeight(30)
        self.btnReset.setFixedHeight(30)
        self.btnAdd.setFixedHeight(30)

        self.yearCombo = QComboBox(self)
        self.yearCombo.addItems(["1st", "2nd", "3rd", "4th"])

        self.branchCombo = QComboBox(self)
        self.branchCombo.addItems([
            "Mechanical", "Chemical", "Software", "Biotech",
            "Computer Science", "Information Technology"
        ])

        self.cACombo = QComboBox(self)
        self.cACombo.addItems([
            "DBMS", "OS", "CN", "C++", "JAVA", "PYTHON", "THERMO",
            "MACHINE", "CELLS", "DS", "CRE", "MICROBES", "FERTILIZER",
            "PLANTS"
        ])

        self.cBCombo = QComboBox(self)
        self.cBCombo.addItems([
            "DBMS", "OS", "CN", "C++", "JAVA", "PYTHON", "THERMO",
            "MACHINE", "CELLS", "DS", "CRE", "MICROBES", "FERTILIZER",
            "PLANTS"
        ])

        self.cCCombo = QComboBox(self)
        self.cCCombo.addItems([
            "DBMS", "OS", "CN", "C++", "JAVA", "PYTHON", "THERMO",
            "MACHINE", "CELLS", "DS", "CRE", "MICROBES", "FERTILIZER",
            "PLANTS", "MOBILE APP"
        ])

        self.rollLabel = QLabel("Roll No")
        self.nameLabel = QLabel("Name")
        self.cALabel = QLabel("Slot A")
        self.yearLabel = QLabel("Current Year")
        self.cBLabel = QLabel("Slot B")
        self.branchLabel = QLabel("Branch")
        self.cCLabel = QLabel("Slot C")

        self.rollText = QLineEdit(self)
        self.nameText = QLineEdit(self)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.rollLabel, 1, 1)
        self.grid.addWidget(self.nameLabel, 2, 1)
        self.grid.addWidget(self.yearLabel, 3, 1)
        self.grid.addWidget(self.branchLabel, 4, 1)
        self.grid.addWidget(self.cALabel, 5, 1)
        self.grid.addWidget(self.cBLabel, 6, 1)
        self.grid.addWidget(self.cCLabel, 7, 1)

        self.grid.addWidget(self.rollText, 1, 2)
        self.grid.addWidget(self.nameText, 2, 2)
        self.grid.addWidget(self.yearCombo, 3, 2)
        self.grid.addWidget(self.branchCombo, 4, 2)
        self.grid.addWidget(self.cACombo, 5, 2)
        self.grid.addWidget(self.cBCombo, 6, 2)
        self.grid.addWidget(self.cCCombo, 7, 2)

        self.grid.addWidget(self.btnReset, 9, 1)
        self.grid.addWidget(self.btnCancel, 9, 3)
        self.grid.addWidget(self.btnAdd, 9, 2)

        self.btnAdd.clicked.connect(self.add_student)
        self.btnReset.clicked.connect(self.reset)
        self.btnCancel.clicked.connect(self.close)

        self.setWindowTitle("Add Student")
        self.resize(400, 350)

    def reset(self):
        self.rollText.clear()
        self.nameText.clear()
        self.yearCombo.setCurrentIndex(0)
        self.branchCombo.setCurrentIndex(0)
        self.cACombo.setCurrentIndex(0)
        self.cBCombo.setCurrentIndex(0)
        self.cCCombo.setCurrentIndex(0)

    def add_student(self):
        db = DBHelper()
        sid = self.rollText.text()
        sname = self.nameText.text()
        dept = self.branchCombo.currentIndex()
        year = self.yearCombo.currentIndex()
        course_a = self.cACombo.currentIndex()
        course_b = self.cBCombo.currentIndex()
        course_c = self.cCCombo.currentIndex()

        if not sid.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Roll number must be a positive integer.')
            return

        sid = int(sid)
        db.add_student(sid, sname, dept, year, course_a, course_b, course_c)
class SearchStudent(QDialog):
    def _init_(self):
        super()._init_()

        self.rollLabel = QLabel("Roll No")
        self.rollText = QLineEdit(self)
        self.searchButton = QPushButton("Search", self)
        self.cancelButton = QPushButton("Cancel", self)

        self.searchButton.setFixedHeight(30)
        self.cancelButton.setFixedHeight(30)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.rollLabel, 1, 1)
        self.layout.addWidget(self.rollText, 1, 2)
        self.layout.addWidget(self.searchButton, 2, 1)
        self.layout.addWidget(self.cancelButton, 2, 2)

        self.searchButton.clicked.connect(self.search_student)
        self.cancelButton.clicked.connect(self.close)

        self.setWindowTitle("Search Student")
        self.resize(300, 150)

    def search_student(self):
        sid = self.rollText.text()

        if not sid.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Roll number must be a positive integer.')
            return

        sid = int(sid)
        db = DBHelper()
        db.search_student(sid)

class DeleteStudent(QDialog):
    def _init_(self):
        super()._init_()

        self.rollLabel = QLabel("Roll No")
        self.rollText = QLineEdit(self)
        self.deleteButton = QPushButton("Delete", self)
        self.cancelButton = QPushButton("Cancel", self)

        self.deleteButton.setFixedHeight(30)
        self.cancelButton.setFixedHeight(30)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.rollLabel, 1, 1)
        self.layout.addWidget(self.rollText, 1, 2)
        self.layout.addWidget(self.deleteButton, 2, 1)
        self.layout.addWidget(self.cancelButton, 2, 2)

        self.deleteButton.clicked.connect(self.delete_student)
        self.cancelButton.clicked.connect(self.close)

        self.setWindowTitle("Delete Student")
        self.resize(300, 150)

    def delete_student(self):
        sid = self.rollText.text()

        if not sid.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Roll number must be a positive integer.')
            return

        sid = int(sid)
        db = DBHelper()
        db.delete_record(sid)

class MainWindow(QMainWindow):
    def _init_(self):
        super()._init_()

        self.setWindowTitle("Student Management System")
        self.setGeometry(100, 100, 600, 400)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")

        addAction = QAction("Add Student", self)
        searchAction = QAction("Search Student", self)
        deleteAction = QAction("Delete Student", self)

        addAction.triggered.connect(self.add_student)
        searchAction.triggered.connect(self.search_student)
        deleteAction.triggered.connect(self.delete_student)

        fileMenu.addAction(addAction)
        fileMenu.addAction(searchAction)
        fileMenu.addAction(deleteAction)

        self.statusBar().showMessage("Ready")

    def add_student(self):
        add_dialog = AddStudent()
        add_dialog.exec()

    def search_student(self):
        search_dialog = SearchStudent()
        search_dialog.exec()

    def delete_student(self):
        delete_dialog = DeleteStudent()
        delete_dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

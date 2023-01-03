"""Install PyQt5 by running the command pip install PyQt5 in your terminal.
Import the necessary modules from PyQt5:"""
import self as self
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

from calculator_by_peter_stoyanov import intro, add, subtract

"""
Create a class for the main window of the application, and set up the layout in the __init__ method:
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Calculator Machine")
        self.setGeometry(100, 100, 400, 200)

        # Create the widgets
        self.intro_label = QLabel(intro())
        self.number1_input = QLineEdit()
        self.number2_input = QLineEdit()
        self.operation_select = QComboBox()
        self.operation_select.addItems(["Add", "Subtract", "Multiply", "Divide"])
        self.calculate_button = QPushButton("Calculate")
        self.result_label = QLabel()

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.intro_label)
        number_layout = QHBoxLayout()
        number_layout.addWidget(self.number1_input)
        number_layout.addWidget(self.operation_select)
        number_layout.addWidget(self.number2_input)
        layout.addLayout(number_layout)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.calculate_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        # Create the main widget and set its layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        # Set the main widget as the central widget
        self.setCentralWidget(main_widget)

"""
Connect the calculate_button to a function that performs the calculation:
"""
self.calculate_button.clicked.connect(self.calculate)


"""
Define the calculate function to perform the calculation based on the selected operation and the input numbers:
"""
def calculate(self):
    # Read the input numbers and the selected operation
    n1 = float(self.number1_input.text())
    n2 = float(self.number2_input.text())
    operation = self.operation_select.currentText()

    # Perform the calculation
def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b
print(intro())
while True:
    choice = input(' 1 - add \n 2 - subtract \n 3 - multiply \n 4 - divide \n 5 - Exit \n What is your choice? :')
    if choice == '5':
        print("thank you for using the machine")
        break

    n1 = float(input("input your first number: "))
    n2 = float(input("input your second number: "))

    if choice == "1":
        print("the result is", add(n1, n2))
    elif choice == "2":
        print("the result is", subtract(n1, n2))
    elif choice == "3":
        print("the result is", multiply(n1, n2))
    elif choice == "4":
        print("the result is", divide(n1, n2))
    else:
        "Wrong Choise! Please Try again."

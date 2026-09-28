import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QGridLayout, QPushButton, QLineEdit, QLabel)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class CalculatorWindow(QMainWindow):
    def __init__(self, logic_engine):
        super().__init__()
        self.logic = logic_engine
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(300, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.display = QLineEdit()
        self.display.setText("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("Arial", 24))
        self.display.setStyleSheet("background-color: #eee; padding: 10px; border: none;")
        main_layout.addWidget(self.display)

        grid_layout = QGridLayout()
        buttons = [
            ('C', 0, 0), ('/', 0, 1), ('*', 0, 2), ('-', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('=', 2, 3, 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 0, 1, 2)
        ]

        for btn_data in buttons:
            text = btn_data[0]
            row = btn_data[1]
            col = btn_data[2]
            r_span = btn_data[3] if len(btn_data) > 3 else 1
            c_span = btn_data[4] if len(btn_data) > 4 else 1

            button = QPushButton(text)
            button.setFont(QFont("Arial", 16))
            button.setMinimumHeight(60)

            if text in ['=', '+', '-', '*', '/', 'C']:
                button.setStyleSheet("background-color: #ff9f43; color: white;")
            else:
                button.setStyleSheet("background-color: #fff;")

            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))

            grid_layout.addWidget(button, row, col, r_span, c_span)

        main_layout.addLayout(grid_layout)

    def on_button_click(self, text):
        if text.isdigit():
            new_val = self.logic.input_digit(text)
        elif text in ['+', '-', '*', '/']:
            self.logic.input_operation(text)
            return
        elif text == '=':
            new_val = self.logic.calculate()
        elif text == 'C':
            new_val = self.logic.clear()
        else:
            return

        self.display.setText(new_val)
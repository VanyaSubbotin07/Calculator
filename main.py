import sys
from PySide6.QtWidgets import QApplication
from calculator_ui import CalculatorWindow
from calculator_logic import CalculatorEngine


def main():
    app = QApplication(sys.argv)
    engine = CalculatorEngine()
    window = CalculatorWindow(engine)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
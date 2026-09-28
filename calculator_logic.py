class CalculatorEngine:
    def __init__(self):
        self.current_input = "0"
        self.first_number = None
        self.operation = None
        self.reset_next = False

    def input_digit(self, digit: str):
        if self.reset_next:
            self.current_input = digit
            self.reset_next = False
        else:
            if self.current_input == "0":
                self.current_input = digit
            else:
                self.current_input += digit
        return self.current_input

    def input_operation(self, op: str):
        try:
            self.first_number = float(self.current_input)
        except ValueError:
            return "Error"

        self.operation = op
        self.reset_next = True
        return self.current_input

    def calculate(self):
        if self.first_number is None or self.operation is None:
            return self.current_input

        try:
            second_number = float(self.current_input)
        except ValueError:
            return "Error"

        result = 0
        if self.operation == '+':
            result = self.first_number + second_number
        elif self.operation == '-':
            result = self.first_number - second_number
        elif self.operation == '*':
            result = self.first_number * second_number
        elif self.operation == '/':
            if second_number == 0:
                return "Err: Div0"
            result = self.first_number / second_number

        self.first_number = None
        self.operation = None
        self.reset_next = True

        if result.is_integer():
            return str(int(result))
        return str(result)

    def clear(self):
        self.current_input = "0"
        self.first_number = None
        self.operation = None
        self.reset_next = False
        return self.current_input
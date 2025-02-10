import math

class Calculator:
    def __init__(self):
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else float('inf')
        }

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, num1, operation, num2):
        if operation not in self.operations:
            raise ValueError("Invalid operation.")
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Inputs must be numbers.")
        return self.operations[operation](num1, num2)

# Advanced operations
def exponentiation(x, y):
    return x ** y

def square_root(x, _):
    return math.sqrt(x)

def logarithm(x, _):
    return math.log(x)

# Main program
if __name__ == "__main__":
    calc = Calculator()
    calc.add_operation('^', exponentiation)
    calc.add_operation('sqrt', square_root)
    calc.add_operation('log', logarithm)
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operation = input("Enter an operation (+, -, *, /, ^, sqrt, log): ")
            num2 = 0 if operation in ['sqrt', 'log'] else float(input("Enter the second number: "))
            
            result = calc.calculate(num1, operation, num2)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        
        cont = input("Do you want to perform another calculation? (y/n): ").lower()
        if cont != 'y':
            break

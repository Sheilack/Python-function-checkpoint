
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

# Dictionary to map operations to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Enter the first number: "))
    
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation. Please select a valid operator.")
            continue
        
        num2 = float(input("Enter the next number: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        user_choice = input(f"Type 'y' to continue with {answer}, or 'n' to start a new calculation: ").lower()
        if user_choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
            
calculator()

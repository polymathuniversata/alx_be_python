def perform_operation(num1, num2, operation):
    """
    Performs arithmetic operations on two numbers.
    
    Args:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide")
        
    Returns:
        float: The result of the operation
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"


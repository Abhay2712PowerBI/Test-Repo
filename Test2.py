
def add_numbers(a, b):
    """
    Adds two numbers after validating the inputs.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of the two numbers.

    Raises:
    ValueError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)):
        raise ValueError("The first argument must be a number.")
    if not isinstance(b, (int, float)):
        raise ValueError("The second argument must be a number.")
    
    return a + b
called_result = add_numbers(5, 10)
print (f"The result of adding is: {called_result}")

def multiply_numbers(a, b):
    """
    Multiplies two numbers after validating the inputs.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The product of the two numbers.

    Raises:
    ValueError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)):
        raise ValueError("The first argument must be a number.")
    if not isinstance(b, (int, float)):
        raise ValueError("The second argument must be a number.")
    
    return a * b
called_result = multiply_numbers(5, 10)
print (f"The result of multiplying is: {called_result}")
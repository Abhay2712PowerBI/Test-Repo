
def add_two_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

# addition demo: read two numbers from input and print their sum
try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
else:
    print(f"Sum: {add_two_numbers(x, y)}")
import sys
import numpy as np


def greet(name):
    """Return a greeting message."""
    return "Hello " + name


def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


def main() -> None:
    print(greet("World"))
    print("Sum of 5 and 7 is:", add_numbers(5, 7))
    print("Python executable path:", sys.executable)
    print("Random number from NumPy:", np.random.rand())


print(
    "This is a very long line that will definitely trigger a flake8 line length warning because it exceeds seventy-nine characters"
)

if __name__ == "__main__":
    main()


import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Check if a number was passed as an argument, else default to 5
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(f"Factorial of {num} is {factorial(num)}")

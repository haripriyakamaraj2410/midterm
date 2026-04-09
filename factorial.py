import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Check if a number was provided via command line, otherwise ask for input
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = int(input("Enter a number: "))
        
    print(f"Factorial of {num} is {factorial(num)}")

# Function to calculate the nth Fibonacci number using recursion
def fibonacci(n):
    # Base cases: first two Fibonacci numbers are 0 and 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive call: sum of previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
num = 6
print("Fibonacci number at position", num, "is:", fibonacci(num))

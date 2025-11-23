# Recursive factorial function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Iterative factorial function
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Loop for multiple inputs
while True:
    num = int(input("Enter a number: "))
    print("Factorial (Recursive):", factorial_recursive(num))
    print("Factorial (Iterative):", factorial_iterative(num))
    
    choice = input("Do you want to calculate another factorial? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting program. Goodbye!")
        break

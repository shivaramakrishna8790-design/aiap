# Function to find the largest number in a list
def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# Take user input for list elements
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Display result
print("The largest number is:", find_largest_number(numbers))

# Function to reverse a string
def reverse_string(s):
    return s[::-1]


# Loop for multiple inputs
while True:
    text = input("Enter a string: ")
    print("Reversed string:", reverse_string(text))
    
    choice = input("Do you want to reverse another string? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting program. Goodbye!")
        break

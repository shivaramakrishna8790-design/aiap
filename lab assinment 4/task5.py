def count_lines_in_file():
    filename = input("Enter the file name: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in '{filename}': {len(lines)}")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

# Run the function
count_lines_in_file()

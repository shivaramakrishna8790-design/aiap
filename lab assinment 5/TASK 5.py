def greet_user(name, gender):
    if gender.lower() == "male":
        title = "Mr."
    elif gender.lower() == "female":
        title = "Ms."
    else:
        title = "Mx."   # Gender-neutral title
    return f"Hello, {title} {name}! Welcome."

# Example
print(greet_user("Alex", "non-binary"))

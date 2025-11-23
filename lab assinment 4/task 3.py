def format_name(full_name):
    parts = full_name.split()
    last = parts[-1]
    first = " ".join(parts[:-1])
    return f"{last}, {first}"

# Examples
print(format_name("John Doe"))
print(format_name("Mary Ann Smith"))
print(format_name("A. B. Clarke"))

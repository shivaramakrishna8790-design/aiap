def loan_approval(name, income, credit_score):
    # Example of potential AI bias (favoring certain names)
    if name.lower() == "john":
        return "Approved"
    elif income > 50000 and credit_score > 700:
        return "Approved"
    else:
        return "Rejected"

# Test cases
print("John:", loan_approval("John", 40000, 600))
print("Mary:", loan_approval("Mary", 60000, 750))
print("Ali:", loan_approval("Ali", 60000, 750))

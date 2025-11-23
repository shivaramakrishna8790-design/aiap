def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Example
print("Sum of first 5 numbers:", sum_to_n_while(5))

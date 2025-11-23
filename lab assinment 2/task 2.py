# ...existing code...
def is_palindrome_number(n: int) -> bool:
    """
    Return True if integer n is a palindrome (reads the same forward and backward).
    Negative numbers are not considered palindromes.
    """
    if n < 0:
        return False
    original = n
    rev = 0
    while n:
        rev = rev * 10 + (n % 10)
        n //= 10
    return original == rev
# ...existing code...

if __name__ == "__main__":
    # No interactive input — predefined test cases and example usage
    test_numbers = [121, -121, 12321, 123, 10, 0]
    for num in test_numbers:
        print(f"{num} -> {is_palindrome_number(num)}")
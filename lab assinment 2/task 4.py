from typing import List
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
def sum_of_squares(nums: List[int]) -> int:
    """
    Return the sum of squares of the numbers in nums.
    Example: sum_of_squares([1,2,3]) -> 1+4+9 = 14
    """
    return sum(x * x for x in nums)
if __name__ == "__main__":
    # Predefined test cases (no user input)
    test_numbers = [121, -121, 12321, 123, 10, 0]
    for num in test_numbers:
        print(f"{num} -> {is_palindrome_number(num)}")
    sample_list = [1, 2, 3, 4, 5]
    print(f"\nSum of squares for {sample_list}: {sum_of_squares(sample_list)}")
# filepath: c:\Users\Sannitha Reddy\OneDrive\Desktop\aa2.4.py
from typing import List
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
def sum_of_squares(nums: List[int]) -> int:
    """
    Return the sum of squares of the numbers in nums.
    Example: sum_of_squares([1,2,3]) -> 1+4+9 = 14
    """
    return sum(x * x for x in nums)
if __name__ == "__main__":
    # Predefined test cases (no user input)
    test_numbers = [121, -121, 12321, 123, 10, 0]
    for num in test_numbers:
        print(f"{num} -> {is_palindrome_number(num)}")
    sample_list = [1, 2, 3, 4, 5]
    print(f"\nSum of squares for {sample_list}: {sum_of_squares(sample_list)}")
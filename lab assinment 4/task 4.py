def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

# Example test cases
print(count_vowels("hello"))   # Output: 2
print(count_vowels("Python"))  # Output: 1
print(count_vowels("AI"))      # Output: 2

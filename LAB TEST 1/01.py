import timeit

# 1️⃣ Using slicing
def reverse_list_slice(lst):
    return lst[::-1]

# 2️⃣ Using reversed()
def reverse_list_reversed(lst):
    return list(reversed(lst))

# 3️⃣ Using a loop (prepend)
def reverse_list_loop(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

# 4️⃣ In-place swapping
def reverse_list_inplace(lst):
    lst = lst.copy()  # avoid modifying original
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# 5️⃣ Using recursion
def reverse_list_recursion(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + reverse_list_recursion(lst[:-1])

# Performance testing
test_list = list(range(10000))
functions = [
    reverse_list_slice,
    reverse_list_reversed,
    reverse_list_loop,
    reverse_list_inplace,
    reverse_list_recursion
]

print("Performance comparison (time for 10 runs):")
for func in functions:
    try:
        time = timeit.timeit(lambda: func(test_list), number=10)
        print(f"{func.__name__}: {time:.5f} seconds")
    except RecursionError:
        print(f"{func.__name__}: RecursionError (too slow for large list)")

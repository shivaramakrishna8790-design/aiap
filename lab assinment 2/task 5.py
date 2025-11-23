# ...existing code...
from typing import Iterable, Tuple
def sum_even_odd(nums: Iterable[int]) -> Tuple[int, int]:
    """Return (sum_of_even_numbers, sum_of_odd_numbers) for nums."""
    even_sum = 0
    odd_sum = 0
    for x in nums:
        if x % 2 == 0:
            even_sum += x
        else:
            odd_sum += x
    return even_sum, odd_sum

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ev_sum, od_sum = sum_even_odd(data)
    print(f"List: {data}")
    print(f"Sum of even numbers: {ev_sum}")
    print(f"Sum of odd numbers: {od_sum}")
# ...existing code...
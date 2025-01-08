def check_if_exist(arr):
    seen = set()
    for num in arr:
        # Check if double or half of the current number exists in the set
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False

# Example usage:
arr = [10, 2, 5, 3]
print(check_if_exist(arr))  # Output: True (5 and 10 satisfy the condition)

def longestCommonPrefixLength(arr1, arr2):
    max_length = 0

    # Convert both arrays' integers to strings for comparison
    arr1 = sorted(map(str, arr1))
    arr2 = sorted(map(str, arr2))

    # Helper function to find common prefix length between two strings
    def commonPrefixLength(a,b):
        length = 0
        # Compare characters one by one until a mismatch
        for i in range(min(len(x), len(y))):
            if a[i] == b[i]:
                length += 1
            else:
                break
        return length

    # Compare all pairs in a sorted manner
    for x in arr1:
        for y in arr2:
            # Break the loop if the first character of x and y don't match (skip unnecessary comparisons)
            if x[0] != y[0]:
                continue

            # Calculate the common prefix length and update the max length
            max_length = max(max_length, commonPrefixLength(x, y))

    return max_length


# Example 1:
arr1 = [10, 1, 100]
arr2 = [1000]
print(longestCommonPrefixLength(arr1, arr2))  # Output: 3

# Example 2:
arr1 = [1, 2, 3,4]
arr2 = [4, 4, 4]
print(longestCommonPrefixLength(arr1, arr2))  # Output: 0

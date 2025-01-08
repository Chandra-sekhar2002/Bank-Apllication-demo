def longestCommonPrefixLength(arr1, arr2):
    max_length = 0

    # Function to find the length of the common prefix between two numbers
    def commonPrefixLength(a, b):
        a_str, b_str = str(a), str(b)
        length = 0

        # Compare digits one by one
        for i in range(min(len(a_str), len(b_str))):
            if a_str[i] == b_str[i]:
                length += 1
            else:
                break

        return length

    # Compare all pairs of numbers from arr1 and arr2
    for x in arr1:
        for y in arr2:
            # Calculate the length of the common prefix for the current pair
            max_length = max(max_length, commonPrefixLength(x, y))

    return max_length


# Example 1:
arr1 = [1,10,100,100]
arr2 = [1000,100,10000]
print(longestCommonPrefixLength(arr1, arr2))  # Output: 3


def getLucky(s,k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)

    def sum_ofdigits(num):
        return sum(int(digit) for digit in str(num))
    result= sum_ofdigits(num_str)
    for i in range(k-1):
        result = sum_ofdigits(result)
    return result
print(getLucky( s = "leetcode", k = 2))


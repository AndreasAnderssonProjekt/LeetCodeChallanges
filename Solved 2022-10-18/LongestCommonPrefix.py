import math
def longestCommonPrefix(strs):
    longest_prefix = 0
    min_length = math.inf
    for str in strs:
        n = len(str)
        if n < min_length:
            min_length = n

    for i in range(min_length):
        c = strs[0][i]
        for str in strs:
            if str[i] != c:
                return strs[0][:longest_prefix]
        longest_prefix += 1
    return strs[0][:longest_prefix]

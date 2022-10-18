def strStr(haystack,needle):
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and i + len(needle) <= len(haystack):
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1

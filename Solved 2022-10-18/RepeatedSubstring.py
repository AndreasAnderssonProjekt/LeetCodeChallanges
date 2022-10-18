def repeatedSubstringPattern( s):
    n = len(s)
    for i in range(1,n // 2):

        if n % i != 0:
            continue
        count = 0

        for j in range(n // i):
            if s[j*i:j*i+i] == s[:i]:
                count += 1
        if count == n // i:
            return True
    return False

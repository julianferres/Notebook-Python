def countUniqueSubstrings(s):
    n = len(s)
    p = 31; m = 10**9+9
    p_pow = [1 for _ in range(n)]

    for i in range(1,n):
        p_pow[i] = (p_pow[i-1]*p)%m

    h = [0 for i in range(n+1)]
    for i in range(n):
        h[i+1] = (h[i]+(ord(s[i])-ord('a')+1) * p_pow[i])%m
    cnt = 0
    for l in range(1,n+1):
        hs = set()
        for i in range(n-l+1):
            cur_h = (h[i+l]+m-h[i])%m
            cur_h = (cur_h*p_pow[n-i-1]) % m
            hs.add(cur_h)
        cnt += len(hs)
    return cnt

print(countUniqueSubstrings('abcaa'))

def discreteLog(a, b, m):
    n = int(m**0.5)+ 1
    an = 1;
    for i in range(n):
        an = (an * a) % m

    vals = {}
    cur = an
    for p in range(1,n+1):
        if not cur in vals:
            vals[cur] = p
        cur = (cur * an) % m

    cur = b
    for q in range(n+1):
        if cur in vals:
            ans = vals[cur] * n - q
            return ans
        cur = (cur * a) % m

    return -1

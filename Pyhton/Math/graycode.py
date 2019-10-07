def g(n):
    return n^(n>>1)

def rev_g(g):
    n = 0
    while(g):
        n^=g
        g>>=1
    return n

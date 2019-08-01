def factmod( n, p ):
    """O(p log n ) aproach to calculate n! (mod p)"""
    if(n>p):
        return 0
    res = 1
    while(n > 1):
        res = (res* (p-1 if((n//p)%2) else 1)) % p;
        for i in range(2, n%p+1):
            res = (res * i) % p
        n //= p

    return res % p;

from random import randint
RAND_MAX = 10**9
def modexp( x, y, p ):
	res = 1
	while(y>0):
		if(y & 1):
			res*= x
			res%=p
		y >>= 1
		x*= x

	return res%p

def check_composite( n, a, d, s):
    x = modexp(a, d, n)
    if (x == 1 or x == n - 1):
        return False
    for r in range(1,s):
        x = x * x % n;
        if (x == n - 1):
            return False

    return True

def MillerRabinProb(n, iter = 5):
    """Returns true if n is probably prime, else returns false."""
    if (n < 4):
        return n == 2 or n == 3

    s = 0;
    d = n - 1;
    while ((d & 1) == 0):
        d >>= 1;
        s+=1

    for i in range(iter):
        a = 2 + randint(1,RAND_MAX) % (n - 3);
        if(check_composite(n, a, d, s)):
            return False
    return True


"""Deterministic Version"""
def MillerRabin(n):
    if(n<2):
        return False

    r = 0
    d = n - 1
    while ((d & 1) == 0):
        d >>= 1
        r+=1

    for a in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}:
        if (n == a):
            return True
        if(check_composite(n, a, d, r)):
            return False
    return True
cnt = 0
for i in range(100000):
    if(MillerRabin(i)):
        cnt+=1
print(cnt)

def is_prime(n):
    """Naive O(sqrt(n)) approach"""
    d = 2
    while(d*d<=x):
        if(x%d == 0):
            return False
        d+=1
    return True

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

def probablyPrimeFermat(n, iter=5):
    if (n < 4):
        return n == 2 or n == 3

    for i in range(iter):
        a = 2 + randint(1, RAND_MAX)%(n - 3);
        if (modexp(a, n - 1, n)!=1):
            return False

    return True

for i in range(100):
    print(i,probablyPrimeFermat(i,5))

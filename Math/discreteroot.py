from math import gcd

def modexp( x, y, p ):
	"""Exponenciacion logaritmica iterativa,
	x^y (mod p), el orden el O(log y)"""

	res = 1
	while(y>0):
		if(y & 1):
			res*= x
			res%=p
		y >>= 1
		x*= x

	return res%p


# Finds the primitive root modulo p
def generator(p):
    fact = []
    phi = p-1
    n = phi
    i = 2
    while(i*i<=n):
        if(n % i == 0):
            fact.append(i);
            while (n % i == 0):
                n //= i
        i+=1

    if(n > 1): fact.push_back(n)

    for res in range(2,p+1):
        ok = True;
        for factor in fact:
            if(modexp(res, phi // factor, p) == 1):
                ok = False
                break
        if(ok): return res
    return -1;

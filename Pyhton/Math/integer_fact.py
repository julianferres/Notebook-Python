"""Naive O(sqrt(n)) approach"""
def trial_division1(n):
    factorization = []
    d = 2
    while(d*d<=n):
        while(n%d == 0):
            factorization.append(d)
            n//=d
        d+=1

    if(n>1):
        factorization.append(n)
    return factorization

"""Don't try even numbers if it's odd. (Wheel factorization)"""
def trial_division2(n):
    factorization = []
    while(n%2 == 0):
        factorization.append(2)
        n >>= 1

    d = 3
    while(d*d<=n):
        while(n%d==0):
            factorization.append(d)
            n //= d
        d+=2
    if(n>1):
        factorization.append(n)
    return factorization

"""Same Wheel idea, but with factors 2,3,5 at the same time."""
def trial_division3(n):
    factorization = []
    for d in {2,3,5}:
        while(n%d==0):
            factorization.append(d)
            n //= d

    increments = [4, 2, 4, 2, 4, 6, 2, 6]
    i = 0
    d = 7
    while(d*d<=n):
        while(n%d == 0):
            factorization.append(d)
            n//= d
        i %= 8
        d+=increments[i]

    if(n>1):
        factorization.append(n)
    return factorization


"""Precomputed primes"""



def trial_division4(n):
    """Fast way to find primes"""
    MAX_PRIME = 10**6
    def listPrimesFast(max_n):
        """sundaram3"""
        numbers = [i for i in range(3, max_n+1, 2)]
        half = (max_n)//2
        initial = 4

        for step in range(3, max_n+1, 2):
            for i in range(initial, half, step):
                numbers[i-1] = 0
            initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

    primes = listPrimesFast(MAX_PRIME)
    factorization = []
    for d in primes:
        if(d*d>n):
            break
        while(n%d == 0):
            factorization.append(d)
            n//=d
    if(n>1):
        factorization.append(n)

    return factorization


"""Pollard's p-1 method"""
from random import randint
from math import gcd
MAX_RAND = 10**9
def pollard_p_minus_1(n):
    """Probabilistic method, O(BlogB log^2 n), encuentra un primo
    que divide a n"""
    MAX_PRIME = 10**6
    def listPrimesFast(max_n):
        """sundaram3"""
        numbers = [i for i in range(3, max_n+1, 2)]
        half = (max_n)//2
        initial = 4

        for step in range(3, max_n+1, 2):
            for i in range(initial, half, step):
                numbers[i-1] = 0
            initial += 2*(step+1)

        if initial > half:
            return [2] + list(filter(None, numbers))

    def modexp( x, y, p ):
    	res = 1
    	while(y>0):
    		if(y & 1):
    			res*= x
    			res%=p
    		y >>= 1
    		x*= x

    	return res%p

    B = 10
    g = 1
    primes = listPrimesFast(MAX_PRIME)
    while(B <= 10**7 and g<n):
        a = 2+ randint(1,MAX_RAND) % (n-3)
        g = gcd(a,n)
        if(g>1):
            return g

        #Computo a^M
        for p in primes:
            if(p>=B):
                continue
            p_power = 1
            while(p_power * p <= B):
                p_power *= p
            a = modexp(a, p_power, n)

            g = gcd(a-1, n)
            if(g>1 and g<n):
                return g
        B*=2

    return 1


"""Pollard Rho algorithm to find a factor of n"""
from math import gcd
def floyd(f, x0):
    tortoise = x0
    hare = f(x0)
    while(tortoise != hare):
        tortoise = f(tortoise)
        hare = f(f(hare))

    return true

mult = lambda a, b, mod: a*b % mod
f = lambda x, c, mod: (mult(x,x,mod)+c)%mod

def rho(n, x0=2, c=1):
    x, y, g = x0, x0, 1
    while(g==1):
        x = f(x, c, n)
        y = f(y, c, n)
        y = f(y, c, n)
        g = gcd(abs(x-y), n)

    return g


"""Brent, direct implementation"""
from math import gcd
mult = lambda a, b, mod: a*b % mod
f = lambda x, c, mod: (mult(x,x,mod)+c)%mod

def brent(n, x0 = 2, c=1):
    x, g, q= x0, 1, 1
    m = 128
    l = 1
    while(g==1):
        y = x
        for i in range(1,l):
            x = f(x, c, n)
        k = 0

        while(k<l and g==1):
            xs = x
            i = 0
            while(i<m and i<l-k):
                x = f(x, c, n)
                q = mult(q, abs(y-x), n)
                i+=1
            g = gcd(q, n)
            k+=m
        l*=2

    if(g==n):
        while True:
            xs = f(xs, c, n)
            g = gcd(abs(xs-y), n)
            if(g!=1 and g!=n):
                break
    return g

from cmath import exp, pi
import sys
sys.path.append("../")

import random
import math
import sys

def miller_rabin(p,s=11):
    #computes p-1 decomposition in 2**u*r
    r = p-1
    u = 0
    while r&1 == 0:#true while the last bit of r is zero
        u += 1
        r = r/2

    # apply miller_rabin primality test
    for i in range(s):
        a = random.randrange(2,p-1) # choose random a in {2,3,...,p-2}
        z = pow(a,r,p)

        if z != 1 and z != p-1:
            for j in range(u-1):
                if z != p-1:
                    z = pow(z,2,p)
                    if z == 1:
                        return False
                else:
                    break
            if z != p-1:
                return False
    return True


def is_prime(n,s=11):
     #lowPrimes is all primes (sans 2, which is covered by the bitwise and operator)
     #under 1000. taking n modulo each lowPrime allows us to remove a huge chunk
     #of composite numbers from our potential pool without resorting to Rabin-Miller
     lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
     if (n >= 3):
         if (n&1 != 0):
             for p in lowPrimes:
                 if (n == p):
                    return True
                 if (n % p == 0):
                     return False
             return miller_rabin(n,s)
     return False

def generate_large_prime(k,s=11):
    #print "Generating prime of %d bits" % k
    #k is the desired bit length

    # using security parameter s=11, we have a error probability of less than
    # 2**-80

    r=100*(math.log(k,2)+1) #number of max attempts
    while r>0:
        #randrange is mersenne twister and is completely deterministic
        #unusable for serious crypto purposes
        n = random.randrange(2**(k-1),2**(k))
        r-=1
        if is_prime(n,s) == True:
            return n
    raise Exception("Failure after %d tries." % r)

def modexp( x, y, p ):
	res = 1
	while(y>0):
		if(y & 1):
			res*= x
			res%=p
		y >>= 1
		x*= x

	return res%p

invMod = lambda y,q:modexp(y,q-2,q)

def generate_primitive_root(n,q):
    if q == 2**64-2**32+1:
        return 7
    not_approved = []

    for i in xrange(q):
        if Prime.is_prime(i):
            s = set()
            for j in range(q):
                s.add(i**j % q)
            if s == set(range(q))-{0}:
                return i
    return None

def ntt(x, q, flag_inverse = False):
    N = len(x)
    assert (q-1) % N == 0 # If this is not true, we won't find a proper k

    # Compute wN at each step
    k = (q-1) / N
    r = generate_primitive_root(N,q)
    wN = pow(r, k, q)
    assert pow(wN, N, q) == 1

    if flag_inverse: # INTT
        wN = invMod(wN, q)

    # End recursion
    if N <= 1: return x

    # Start recursion
    even = ntt(x[0::2], q, flag_inverse)
    odd =  ntt(x[1::2], q, flag_inverse)

    # Apply the transform at each step
    T= [pow(wN, k, q) * odd[k] % q for k in xrange(N/2)]
    return [(even[k] + T[k]) % q for k in xrange(N/2)] + [(even[k] - T[k]) % q for k in xrange(N/2)]

def intt(x,q):
    N = len(x)
    assert (q-1) % N == 0 # If this is not true, we won't find a proper k

    return [y*invMod(N,q)%q for y in ntt(x, q, -1)]

def mul(a, b, q):
    return [x * y % q for x,y in zip(a,b)]

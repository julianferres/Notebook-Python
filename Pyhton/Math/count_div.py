def countDivisors(n):
    """Naive implementation to count divisors of n, in O(sqrt(n))"""
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if (n % i == 0):
            cnt += 1 if(i*i == n) else 2

    return cnt



"""Improved method in O(n^(1/3))"""
def SieveOfEratosthenes(n, prime,primesquare, a):
    """Sieve of primes and squares of primes."""
    for i in range(2,n+1):
        prime[i] = True

    for i in range((n * n + 1)+1):
        primesquare[i] = False

    prime[1] = False

    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            i = p * 2
            while(i <= n):
                prime[i] = False
                i += p
        p+=1

    j = 0
    for p in range(2,n+1):
        if (prime[p]==True):
            a[j] = p

            primesquare[p * p] = True
            j+=1

def countDivisorsFast(n):
    """Count divisors in O(n^(1/3))"""
    if (n == 1):
        return 1

    prime = [False]*(n + 2)
    primesquare = [False]*(n * n + 2)

    a = [0]*n

    SieveOfEratosthenes(n, prime, primesquare, a)

    ans = 1

    i=0
    while(1):
        if(a[i]**3 > n):
            break

        cnt = 1
        while (n % a[i] == 0):
            n //= a[i]
            cnt += 1
        ans *= cnt
        i+=1

    if(prime[n]==True):
        ans *= 2

    elif(primesquare[n]==True):
        ans *= 3

    elif(n != 1):
        ans *= 4

    return ans

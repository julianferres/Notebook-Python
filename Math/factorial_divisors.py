# Count of divisors of n!

allPrimes = []
def sieve(n):
    prime = [True] * (n + 1)

    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            i = p * 2
            while(i <= n):
                prime[i] = False
                i += p
        p += 1

    for p in range(2, n + 1):
        if (prime[p]):
            allPrimes.append(p)

def factorialDivisors(n):

    sieve(n)
    result = 1

    for i in range(len(allPrimes)):
        p = allPrimes[i]
        exp = 0
        while (p <= n):
            exp += n // p
            p *= allPrimes[i]

        result *= (exp + 1)

    return result

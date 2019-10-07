# Program to fiind prime factors and their powers
# using Sieve Of Eratosthenes

def sieveOfEratosthenes(N, s):
    """Sieve with smaller prime factor of s[i]"""

    prime = [False] * (N+1)

    for i in range(2, N+1, 2):
        s[i] = 2

    for i in range(3, N+1, 2):
        if (prime[i] == False):
            s[i] = i

            for j in range(i, N//i + 1, 2):
                if (prime[i*j] == False):
                    prime[i*j] = True
                    s[i * j] = i


def generatePrimeFactors(N):

    #s[i]: smallest prime factor
    s = [0] * (N+1)
    sieveOfEratosthenes(N, s)

    factors = [] #Contains tuples (p_i, alpha_i)

    curr = s[N]
    # Power of current prime factor
    cnt = 1

    while (N > 1):
        N //= s[N]

        if (curr == s[N]):
            cnt += 1
            continue

        factors.append((curr,cnt))
        curr = s[N]
        cnt = 1
    return factors

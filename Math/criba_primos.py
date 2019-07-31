"""Criba sin optimizar, O(n* log log n)"""

n = 10**6
is_prime = [True]*(n+1)

is_prime[0] = False
is_prime[1] = False

for i in range(2,n+1):
	if(is_prime[i] and i*i<=n):
		for j in range(i*i,n+1,i):
			is_prime[j] = False


"""Sieving till root"""

n = 10**6
is_prime = [True]*(n+1)

is_prime[0] = False
is_prime[1] = False

for i in range(2,n+1):
	if(is_prime[i]):
		for j in range(i*i,n+1,i):
			is_prime[j] = False



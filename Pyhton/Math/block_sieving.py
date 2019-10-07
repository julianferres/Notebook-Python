"""Cuento los primos menores a n usando block_sieving"""

def count_primes(n):
	S = 10000
	primes = []
	nsqrt = int(n**0.5)
	is_prime = [True]*(nsqrt+1)

	for i in range(2, nsqrt+1):
		if(is_prime[i]):
			primes.append(i)
			for j in range(i*i,nsqrt+1,i):
				is_prime[j] = False

	result = 0
	block = [True]*S

	k = 0
	while(k*S <= n):
		block = [True]*S
		start = k*S

		for p in primes:
			start_idx = (start+p-1)//p
			j = max(start_idx, p )* p - start
			while(j<S):
				block[j] = False
				j+=p

		if( k == 0):
				block[0] = False
				block[1] = False
		i = 0
		while(i<S and start+i <= n):
			if(block[i]):
				result+=1
			i+=1
		k+=1

	return result

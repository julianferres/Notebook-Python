def compute_hash(s):
	p = 31 #Cambiar esto por un primo un poco mas grande
	m = 10**9+9
	p_pow = 1
	hash_value = 0
	for c in s:
		hash_value = (hash_value + (ord(c)-ord('a')+1)*p_pow)%m
		p_pow = (p_pow * p)%m
	return hash_value

def groupIdenticalStrings(s):
	"""Recibo una lista de strings, devuelvo los grupos de strings identicas
	O(n*m+n*log n) (n=len(s), m = maxlen entre las strings"""
	n = len(s)
	hashes = [None for i in range(n)]
	for i in range(n):
		hashes[i] = (compute_hash(s[i]),i)
	hashes.sort()
	groups = []
	for i in range(n):
		if(i==0 or hashes[i][0] != hashes[i-1][0]):
			groups.append([])
		groups[-1].append(hashes[i][1])
	return groups

print(groupIdenticalStrings(["aaa","bca","aaa","amclakm"]))

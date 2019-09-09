def compute_hash(s):
	p = 31 #Cambiar esto por un primo un poco mas grande
	m = 10**9+9
	p_pow = 1
	hash_value = 0
	for c in s:
		hash_value = (hash_value + (ord(c)-ord('a')+1)*p_pow)%m
		p_pow = (p_pow * p)%m
	return hash_value



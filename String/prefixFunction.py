def prefixFunction(s):
	"""Devuelve un array pi, donde pi[i] 
	coincide con el mayor prefijo propio que ademas
	es sufijo de s[0...i]"""
	n = len(s)
	pi = [0 for _ in range(n)]
	
	for i in range(1,n):
		j = pi[i-1]
		while(j>0 and s[i]!=s[j]):
			j = pi[j-1]
		if(s[i]==s[j]): j+=1
		pi[i] = j

	return pi

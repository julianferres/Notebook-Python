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

def KMP(s,t):
	"""Encuentra todas las ocurrencias de s en t en
	O(|s|+|t|)"""
	n = len(s); m = len(t)
	separator = "#" 
	#Elegir algun caracter que no este en s ni en t

	pi = prefixFunction(s+separator+t)
	occurences = []

	for i in range(n+1,n+m+1):
		if(pi[i]==n): occurences.append(i-2*n)
	return occurences

print(prefixFunction("ab#abab"))
print(KMP("ab","abab"))


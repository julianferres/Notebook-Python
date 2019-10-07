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

def numOccurencesPrefix(s):
	"""Cuenta el numero de apariciones de 
	cada prefijo de s en s"""
	pi = prefixFunction(s)
	n = len(s)
	ans = [0 for i in range(n+1)]
	for i in range(n):
		ans[pi[i]]+=1
	i = n-1
	while(i>0):
		ans[pi[i-1]] += ans[i]
		i-=1
	for i in range(n+1):
		ans[i]+=1
	return ans

def numDifferentSubstring(s):
	"""Dada una string s, cuenta la cantidad de
	substrings diferentes que contiene. O(|s|^2)"""
	ans = 1; n = len(s)
	for i in range(1,n):
		pimax = max(prefixFunction(s[:i+1][::-1]))
		ans += i+1-pimax
	return ans

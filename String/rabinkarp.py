def rabin_karp(s, t):
	"""O(|s|+|t|). Given a pattern s and a text t,
	determine if the pattern appears in the text and if it does,
	enumerate all its occurrences."""
	p = 31
	m = 10**9+9
	S = len(s); T = len(T)
	p_pow = [1 for _ in range(max(S,T))]
	for i in range(1,len(p_pow)):
		p_pow[i] = (p_pow[i-1]*p)%m
	h = [0 for i in range(T+1)]
	for i in range(T):
		h[i+1] = (h[i]+ (ord(t[i])-ord('a')+1)*p_pow[i])%m
	h_s = 0
	for i in range(S):
		h_s = (h_s + (ord(s[i])-ord('a')+1)*p_pow[i])%m

	occurences = []
	for i in range(T-S+1):
		cur_h = (h[i+S]-h[i])%m
		if(cur_h == h_s * p_pow[i]%m):
			occurences.append(i)
	return occurences

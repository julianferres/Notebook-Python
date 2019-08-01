def modexp( x, y, p ):
	"""Exponenciacion logaritmica iterativa,
	x^y (mod p), el orden el O(log y)"""

	res = 1
	while(y>0):
		if(y & 1):
			res*= x
			res%=p
		y >>= 1
		x*= x

	return res%p



"""Inverso si m es primo"""
modinv = lambda a, m : modexp(a, m-2, m)

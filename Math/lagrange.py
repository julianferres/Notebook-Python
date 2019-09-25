def interpolacion(muestra, x):
	"""Recibe una muestra de n puntos (tuplas (xi,yi))
	y evalua el polinomio de Lagrange de 
	en el punto x desconocido"""
	ans = 0
	n = len(muestra)
	for i in range(n):
		term = muestra[i][1]
		for j in range(n):
			if(j!=i):
				term = term*(x-muestra[j][0])/(muestra[i][0]-muestra[j][0])
		ans+=term
	return ans
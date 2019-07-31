def turn( p, q, r):
	"""Recibe tres puntos p, q y r (2D) y
		devuelve si se encuentran en sentido horario,
		antihorario o alineados"""
	
	result = (r[0]-q[0])*(p[1]-q[1]) - (r[1]-q[1])*(p[0]-q[0])
	
	if(result < 0): 
		return -1 # P->Q->R es una terna derecha (CCW)

	if(result > 0): 
		return 1 # P->Q->R es una terna izquierda

	return 0 # P->Q->R colineales

# Wrapper para chequear directamente CCW, si se toleran colineales usar >=
ccw = lambda p, q, r: turn(p, q, r)>0



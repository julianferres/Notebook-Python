def determinant(puntos):
	"""Recibe una lista de puntos (tuplas 2D)
	y calcula su -determinante-"""
	result = 0
	size = len(puntos)
	for i in range(size):
		x1, x2 = puntos[i][0], puntos[(i+1)%size][0]
		y1, y2 = puntos[i][1], puntos[(i+1)%size][1]
	
		result += (x1*y2-x2*y1)

	return result


		
		


		

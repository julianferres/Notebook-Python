from math import sqrt
def perimeter(puntos):
	"""Recibe una lista de puntos 2D que representan
		los vertices de un poligono y devuelve el perimetro
		del mismo."""
	result = 0
	size = len(puntos)
	for i in range(size):
		x1, x2 = puntos[i][0], puntos[(i+1)%size][0]
		y1, y2 = puntos[i][1], puntos[(i+1)%size][1]
		dx, dy = x2-x1, y2-y1
		result += sqrt(dx**2+dy**2)
	
	return result



def floydWarshall(adyMatrix):
	"APSP problem, O(V^3)"
	v = len(adyMatrix)
	for k in range(v):
		for i in range(v):
			for j in range(v):
				adyMatrix[i][j] = min(adyMatrix[i][j],adyMatrix[i][k]+adyMatrix[k][j])


def transitiveClosure(d):
	"""d[i][j] tiene 1 si hay un camino enre i y j,
	 0 en caso contrario, O(V^3)"""
	v = len(d)
	for k in range(v):
		for i in range(v):
			for j in range(v):
				d[i][j] |= (d[i][k] & d[k][j])


def minimax(d):
	"""Encuentra el minimo entre los maximos edges de cada path"""
	v = len(d)
	for k in range(v):
		for i in range(v):
			for j in range(v):
				d[i][j] = min(d[i][k], max(d[i][k],d[k][j]))

def maximin(d):
	v = len(d)
	for k in range(v):
		for i in range(v):
			for j in range(v):
				d[i][j] = max(d[i][j], min(d[i][k],d[k][j]))



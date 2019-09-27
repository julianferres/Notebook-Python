visited = set()
orden = []
def dfs(ady , v):
	orden.append(v); visited.add(v)
	for u in ady[v]:
		if u not in visited:
			dfs(ady,u)

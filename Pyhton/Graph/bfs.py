from collections import deque
def bfs(ady, s):
	vis = set()
	parent = {}; dist = {}

	q = deque([])
	q.append(s); vis.add(s); parent[s]=-1; dist[s]=0

	while q:
		v = q.popleft()
		for u in ady[v]:
			if u not in vis:
				vis.add(u)
				q.append(u)
				dist[u] = dist[v]+1
				parent[u] = v
	return vis,parent,dist

def SSSP(ady, src, dst):
	"""Single-source shortest path"""
	vis, par , dist = bfs(ady,src)
	path = []
	if(dst not in vis): return path
	while(dst!=src):
		path.append(dst)
		dst = par[dst]
	path.append(src)
	return path[::-1]

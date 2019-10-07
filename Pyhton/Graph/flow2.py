from collections import deque
from math import inf

class Graph:
	def __init__(self, ady, cap):
		self.n = len(cap)
		self.ady = ady
		self.cap = cap

	def bfs(self,s, t, parent):
		q = deque([])
		parent[s] = -2; q.append((s,inf))

		while(q):
			cur, flow = q[0][0], q[0][1]
			q.popleft()
			for next in self.ady[cur]:
				if(parent[next]==-1 and cap[cur][next]):
					parent[next] = cur
					new_flow = min(flow, cap[cur][next])
					if(next==t):
						return new_flow
					q.append((next,new_flow))
		return 0
	def FordFulkerson(self,s,t):
		flow = 0
		parent =  [-1]*self.n
		new_flow = self.bfs(s,t,parent)
		while(new_flow):
			flow+=new_flow
			cur = t
			while(cur!= s):
				prev = parent[cur]
				cap[prev][cur] -= new_flow
				cap[cur][prev] += new_flow
				cur = prev

			parent = [-1]*self.n
			new_flow = self.bfs(s,t,parent)
		return flow

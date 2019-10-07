from collections import deque
from math import inf
class Graph:
    def __init__(self, cap):
        self.n = len(cap)
        self.cap = cap
        self.org_cap = [i[:] for i in cap]
    def bfs(self,s,t,parent):
        visited = [False]*(self.n)
        queue = deque([])
        queue.append(s); visited[s]=True
        while queue:
            u = queue.popleft()
            for ind,val in enumerate(self.cap[u]):
                if(not visited[ind] and val):
                    queue.append(ind)
                    visited[ind]=True
                    parent[ind] = u
        return visited[t]

    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.n)
        max_flow = 0
        while self.bfs(source,sink,parent):
            path_flow = inf
            s = sink
            while(s!=source):
                path_flow = min(path_flow,self.cap[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while(v!= source):
                u = parent[v]
                self.cap[u][v] -= path_flow
                self.cap[v][u] += path_flow
                v = parent[v]
        return max_flow


    def minCut(self, source, sink):
        def dfs(s,visited):
            visited[s] = True
            for u in range(self.n):
                if (not visited[u] and self.cap[s][u]>0):
                    dfs(u,visited)
        g.FordFulkerson(source,sink)
        print(g.cap)
        vis = [False]*self.n
        dfs(source,vis)
        cut = []
        for i in range(self.n):
            for j in range(self.n):
                if(vis[i] and not vis[j] and self.org_cap[i][j]):
                    cut.append((i,j))
        return cut

class Vertex(object):
	"""docstring for Vertex."""

	def __init__(self, node):
		self.id = node
		self.adyacent = {}

	def __str__(self):
		return str(self.id)+'adjacent: '+str([x.id for x in self.adyacent])

	def add_neighbor(self, neigbhor, weight = 0):
		self.adyacent[neigbhor] = weight

	def get_connections(self):
		return self.adyacent.keys()

	def get_id(self):.
		return self.id

	def get_weight(self, neighbor):
		return self.adjacent[neighbor]


class Graph:
	def __init__(self):
		self.vert = {}
		self.num_vertices = 0

	def __iter__(self):
		return iter(self.vert.values())

	def add_vertex(self, node):
		self.num_vertices+=1
		new_vertex = Vertex(node)
		self.vert[node] = new_vertex
		return new_vertex

	def get_vertex(self, n):
		return self.vert[n] if(n in self.vert) else None

	def add_edge(self, from, to, weight):
		if from not in self.vert:
				self.add_vertex(from)
		if to not in self.vert:
				self.add_vertex(to)
		self.vert[from].add_neighbor(self.vert[to],weight)
		self.vert[to].add_neighbor(self.vert[from],weight)

	def get_vertices(self):
		return self.vert.keys()

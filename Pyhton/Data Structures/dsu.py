class DisjointSetUnion:
    def __init__(self, array):
        self.parent = [i for i in array]
        self.rank = [0 for _ in range(len(array))]
        self.size = [1] * (len(array) + 1)
        self.group = [[a[i]] for i in array]

    def find(self, x):
        # If x is root
        if self.parent[x] == x:
            return x
        # If x is not root, search again by using x's parent
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # Make an edge from the root of lower tree to the root of higher tree
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            # If the height of tree the tree is the same, increase one of the heights by 1
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if len(self.group[x]) < len(self.group[y]):
            x, y = y, x
        self.group[x].extend(self.group[y])
        self.group[y] = []
        self.parent[y] = x

    def check_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

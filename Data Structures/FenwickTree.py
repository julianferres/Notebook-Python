class FenwickTreeSum:
    """ BIT de Sumas,
    Resuelve las queries de intervalos y modificacion del array original
    en O(log n)."""
    def __init__(self, n):
        self.bit = [0]*n #Binary Indexed Tree
        self.n = n

    def initArray(self, array):
        for i in range(len(array)):
            self.update(i, array[i])

    def sum(self, r):
        ret = 0
        while(r>=0):
            ret += self.bit[r]
            r = (r&(r+1))-1

        return ret

    def rangeSum(self, l, r):
        return self.sum(r)-self.sum(l-1)

    def update(self, idx, delta): #Add delta to a[idx]
        while(idx<self.n):
            self.bit[idx] += delta
            idx |= (idx+1)



from math import inf
class FenwickTreeMin:
    """ BIT de Min,
    Resuelve las queries de intervalos y modificacion del array original
    en O(log n)."""
    def __init__(self, n):
        self.bit = [inf]*n #Binary Indexed Tree
        self.n = n

    def initArray(self, array):
        for i in range(len(array)):
            self.update(i, array[i])

    def getMin(self, r):
        ret = inf
        while(r>=0):
            ret = min(ret, self.bit[r])
            r = (r&(r+1))-1

        return ret


    def update(self, idx, val):
        while(idx<self.n):
            self.bit[idx] = min(self.bit[idx], val)
            idx |= (idx+1)

"""Revisar
class FenwickTreeSum2D:
    def __init__(self, n, m):
        self.bit = [[0]*(m+1) for _ in range(n+1)] #Binary Indexed Tree 2D
        self.n = n
        self.m = m

    def initArray(self,array):
        aux = [[0]*(self.m+1) for _ in range(self.n+1)]
        for i in range(1,self.n+1):
            for j in range(1,self.m+1):
                aux[i][j] = array[self.n-j][i-1]
        #It's a matrix now
        for j in range(1,self.m+1):
            for i in range(1,self.n+1):
                v1 = self.getSum(i,j)
                v2 = self.getSum(i,j-1)
                v3 = self.getSum(i-1,j-1)
                v4 = self.getSum(i-1,j)
                self.update(i,j,aux[i][j]-(v1-v2-v4+v3))

    def getSum(self, i, j):
        suma = 0
        while(i>0):
            while(j>0):
                suma += self.bit[i][j]
                j = (j & (j+1))-1
            i = (i & (i+1))-1
        return suma


    def update( self, i, j, val):
        while( i <= self.n ):
            while(j <= self.m):
                self.bit[i][j] += val
                j |= (j+1)
            i |= (i+1)

    def answerQuery(self,i1,j1, i2, j2):
        ans = self.getSum(i2+1, j2+1)-self.getSum(i2+1, j1)-self.getSum(i1, j2+1)+self.getSum(i1, j1)

        return ans
"""

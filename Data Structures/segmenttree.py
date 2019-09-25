class SegmentTree:
    """Segment tree of sums"""

    def __init__(self, array):
        self.n = len(array)
        self.t = [0]*self.n + array

        for i in range(self.n-1, 0, -1):
            self.t[i] = self.t[i<<1]+ self.t[(i<<1)|1]

    def modify(self, idx, val):
        idx+=self.n; self.t[idx] = val
        while(idx>1):
            self.t[idx>>1] = self.t[idx] + self.t[idx^1]
            idx >>=1

    def modifyInterval(self, l, r, value):
        """Modifica intervalo [l,r) poniendo value"""
        l+=self.n; r+=self.n
        while(l<r):
            if(l&1):
                l+=1; self.t[l]+= value
            if(r&1):
                r-=1; self.t[r] += value
            l>>=1; r>>=1

    def push(self):
        """Si necesitamos inspeccionar todos los elementos del array,
        es conveniente pushear la info a las hojas, reduce O(nlogn) a O(n)
        """
        for i in range(1,self.n):
            self.t[i<<1] += self.t[i]
            self.t[(i<<1)|1] += self.t[i]
            self.t[i] = 0

    def query(self, l, r):
        """Responde al intervalo [l,r)"""
        res = 0 #Se usa el neutro de la operacion
        l+=self.n ; r+=self.n

        while(l<r):
            if(l&1):
                res += self.t[l]
                l+=1
            if(r&1):
                r-=1
                res += self.t[r]
            l>>=1; r>>=1

        return res

    def queryElement(self, p):
        """Devuelve el valor de un elemento"""
        res = 0 ; p+= self.n
        while(p>0):
            res+= self.t[p]
            p>>=1
        return res


a = SegmentTree([1,2,3,4])
a.modifyInterval(0,3,10)
print(a.queryElement(3))
print(a.t)

class SegmentTreeGeneric:
    """Generic Segment Tree. f es una funcion asociativa"""

    def __init__(self, array, f):
        self.n = len(array)
        self.t = [0]*self.n + array
        self.f = f #Me guardo la funcion aca para los otros metodos

        for i in range(self.n-1, 0, -1):
            self.t[i] = self.f(self.t[i<<1],self.t[(i<<1)|1])

    def modify(self, idx, val):
        idx+=self.n; self.t[idx] = val
        while(idx>1):
            self.t[idx>>1] = self.f(self.t[idx] + self.t[idx^1])
            idx >>=1

    def query(self, l, r):
        res = 0 #Se usa el neutro de la operacion
        l+=self.n ; r+=self.n
        
        while(l<r):
            if(l&1):
                res = self.t[l] if res==0 else self.f(res,self.t[l])
                l+=1
            if(r&1):
                r-=1
                res = self.t[r] if res==0 else self.f(self.t[r],res)
            l>>=1; r>>=1

        return res

"""Find all invmods in range [1,m-1] in O(m)"""
def allModInvs(m):
    inv = [1]*(m) #Remember that inv[i] has the inverse of i
    inv[0] = None
    for i in range(2,m):
        inv[i] = -(m//i)*inv[m%i] %m

    return inv

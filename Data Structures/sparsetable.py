from math import log

MAXN = 10**7 #Biggest possible array lenght
K = 25 # Must satisfy K >= floor(log_2{MAXN})+1

"""Generic precomputation"""
def precomputation(array, f):
    n = len(array)
    K = int(log(n,2))+1
    st = [[None for __ in range(K)] for _ in range(n)]

    for i in range(n):
        st[i][0] = f([array[i]])
    for j in range(1,K+1):
        for i in range(n-(1<<j)+1):
            st[i][j] = f([st[i][j-1], st[i+(1<<(j-1))][j-1]])

    return st

"""Range Sum Queries"""
array = [1, 4, -1, 6, 9]
n = len(array)
K = int(log(n,2))+1
st = precomputation(array, sum)

def rangeSumQuery(L, R):
    sum = 0
    for j in range(K,-1,-1):
        if((1<<j) <= R-L+1):
            sum+= st[L][j]
            L += 1<<j

    return sum


"""Range Minimun Queries (RMQ)"""
def precomputeLogs(n):
    logs = {1:0}
    for i in range(2,n+1):
        logs[i] = logs[i//2] + 1

    return logs

array = [1, 4, -1, 6, 9]
n = len(array)
K = int(log(n,2))+1
st = precomputation(array, min)
logs = precomputeLogs(n)

def rangeMinimumQuery( L, R):
    j = logs[R-L+1]
    return min(st[L][j], st[R-(1<<j)+1][j])

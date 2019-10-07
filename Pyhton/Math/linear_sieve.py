N = 10**6
lp = [0]*(N+1)
pr = []

import timeit
start = timeit.default_timer()
for i in range(2,N+1):
    if(lp[i]==0):
        lp[i]=i
        pr.append(i)

    j = 0
    while(j<len(pr) and pr[j]<=lp[i] and i*pr[j]<=N):
        lp[i*pr[j]] = pr[j]
        j+=1
end = timeit.default_timer()
print(end-start)

print(lp[:20])
print(pr[:20])

from bisect import bisect_right
import heapq
def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    return i if i != len(a) else -1

def LIS(arr):
    piles = []

    for idx in range(len(arr)):
        aux = [piles[i][-1] for i in range(len(piles))]
        pileNumber = find_gt(aux,arr[idx])
        if(pileNumber==-1):
            piles.append([arr[idx]])
        else:
            piles[pileNumber].append(arr[idx])

    print(piles)
    aux = [piles[i][::-1] for i in range(len(piles))]
    orden = list(heapq.merge(*aux))
    print(orden)

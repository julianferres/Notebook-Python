class Point:
    """2D-Point representation"""


def sign(x):
    if x >= 0: return 1
    else: return 0
def triads(p):
    return zip(p, p[1:]+[p[0]], p[2:]+[p[0]]+[p[1]])
 
def check_convexity(p):
    i = 0
    for ((x0, y0), (x1, y1), (x2,y2)) in triads(p):
        if i==0: fsign = sign(x2*(y1-y0)-y2*(x1-x0)+(x1-x0)*y0-(y1-y0)*x0)
        else:
            newsign = sign(x2*(y1-y0)-y2*(x1-x0)+(x1-x0)*y0-(y1-y0)*x0)
            if newsign != fsign: return False
        i +=1
    return True
 
 
 
 
def reflejo(x1,y1,x2,y2):
    return 2*x2-x1, 2*y2-y1
 
def son_paralelas(d1,d2):
    return d2[0]*d1[1] == d1[0]*d2[1]
 
def mediatriz(x1,y1,x2,y2):
    return (y2-y1,x1-x2),((x1+x2)/2,(y1+y2)/2)
 
 
def solve_eq(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
 
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
 
    div = det(xdiff, ydiff)
    if div == 0:
        return False
 
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y
 
def solve(x1,y1,x2,y2,x3,y3):
 
    d1, of_m1 = mediatriz(x1,y1,x2,y2) 
    d2, of_m2 = mediatriz(x2,y2,x3,y3) 
 
 
 
    t = solve_eq([(d1[0]+of_m1[0], d1[1]+of_m1[1]),of_m1],[(d2[0]+of_m2[0], d2[1]+of_m2[1]),of_m2])
    if not t:
        return False
 
 
    j1 = solve_eq(((d1[0]+t[0],d1[1]+t[1]),t),((d2[0]+x2,d2[1]+y2),(x2,y2)))
    j2 = solve_eq(((d1[0]+x2,d1[1]+y2),(x2,y2)),((d2[0]+t[0],d2[1]+t[1]),t))
 
    if(not j1 or not j2):
        return False
 
    A = reflejo(t[0],t[1],j1[0],j1[1])
    if(son_paralelas((A[0]-x2,A[1]-y2),(x3-x2, y3-y2))):
        return False
    B = reflejo(t[0],t[1],j2[0],j2[1])
    if(son_paralelas((B[0]-x2,B[1]-y2),(x1-x2, y1-y2))):
        return False
 
 
    D = reflejo(A[0],A[1],x1,y1)
    C = reflejo(B[0],B[1],x3,y3)
 
    if(check_convexity([A,B,C,D])):
 
        return A,B,C,D
    else:
        return False
from functools import reduce
def convex_hull_graham(points):
    TURN_LEFT, TURN_RIGHT, COLLINEAR = (1, -1, 0)
    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) not in {TURN_LEFT}:
        	#Agregar a {TURN_LEFT} el elemento COLLINEAR si se quieren alineados en
        	#En la frontera
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

def gcd(a, b):
    """Devuelve el gcd entre a y b, y coefx y coefy tales
    que a*coefx+b*coefy = gcd"""
    if(a==0):
        return b, 0, 1
    g, x1, y1 = gcd(b%a, a)
    x = y1-(b//a)*x1
    y = x1
    return g, x, y

def find_any_solution(a, b, c):
    """Returns g = gcd(a,b) and a pair of coef x0, y0 such that
    a*x0+b*y0 = g"""
    g, x0, y0 = gcd(abs(a), abs(b))
    if (c % g):
        return False

    x0 *= c // g;
    y0 *= c // g;
    if (a < 0): x0 = -x0;
    if (b < 0): y0 = -y0;
    return g, x0, y0


def shift_solution(x, y, a, b, cnt):
    """Dada una solucion a la ecuacion diofantica, encuentra otra"""
    x += cnt * b;
    y -= cnt * a;
    return x, y


def find_all_solutions( a, b, c, minx, maxx, miny, maxy):
    sol = find_any_solution(a, b, c)
    if (not sol):
        return 0
    g, x, y = sol
    a //= g
    b //= g

    sign_a = 1 if(a > 0) else -1
    sign_b = 1 if(b > 0) else -1

    x, y = shift_solution(x, y, a, b, (minx - x) // b)
    if (x < minx):
        x, y = shift_solution(x, y, a, b, sign_b)
    if (x > maxx):
        return 0
    lx1 = x

    x, y = shift_solution(x, y, a, b, (maxx - x) // b);
    if (x > maxx):
        x, y = shift_solution(x, y, a, b, -sign_b)
    rx1 = x

    x, y = shift_solution(x, y, a, b, -(miny - y) // a)
    if (y < miny):
        x, y = shift_solution(x, y, a, b, -sign_a)
    if (y > maxy):
        return 0
    lx2 = x

    x, y = shift_solution(x, y, a, b, -(maxy - y) // a)
    if (y > maxy):
        shift_solution(x, y, a, b, sign_a)
    rx2 = x

    if (lx2 > rx2):
        lx2, rx2 = rx2, lx2
    lx = max(lx1, lx2);
    rx = min(rx1, rx2);

    if (lx > rx):
        return 0

    # Para enumerarlas, basta iterar desde x = lx+ k*b//g, el numero
    # necesario de soluciones

    return (rx - lx) // abs(b) + 1;

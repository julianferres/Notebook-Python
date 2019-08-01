def gcd(a, b):
    """Devuelve el gcd entre a y b, y coefx y coefy tales
    que a*coefx+b*coefy = gcd"""
    if(a==0):
        return b, 0, 1
    d, x1, y1 = gcd(b%a, a)
    x = y1-(b//a)*x1
    y = x1
    return d, x, y


def modinv(a, m):
    g, x, y = gcd(a,m)
    if(g!=1):
        return None
    x = (x%m + m)%m
    return x

def logmul(a, b):
    """No creo que sea necesario en python, pero version recursiva
    de la multiplicacion que sirve en C++"""
    if(a == 0):
        return 0
    return 2*logmul((a-1)//2,b)+b if(a%2) else 2*logmul(a//2,b)


def logmulmod(a, b, p):
    """Multiplicacion recursiva mod p"""
    if(a == 0):
        return 0

    res = 2*logmulmod((a-1)//2,b, p)+b if(a%2) else 2*logmulmod(a//2,b, p)
    return res%p

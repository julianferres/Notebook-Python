gcd = lambda a, b : a if(b==0) else gcd(b,a%b)

def it_gcd(a, b):
    while(b):
        a%=b
        a, b = b, a #Swap para tener el mas chico en b
    return a

from cmath import exp
from math import pi

# A simple class to simulate n-th root of unity
class NthRootOfUnity:
    def __init__(self, n, k = 1):
        self.k = k
        self.n = n

    def __pow__(self, other):
        if type(other) is int:
            n = NthRootOfUnity(self.n, self.k * other)
            return n

    def __eq__(self, other):
        if other == 1:
            return abs(self.n) == abs(self.k)

    def __mul__(self, other):
        return exp(2*1j*pi*self.k/self.n)*other

    def __repr__(self):
        return str(self.n) + "-th root of unity to the " + str(self.k)

    @property
    def th(self):
        return abs(self.n // self.k)


""" The Fast Fourier Transform Algorithm

 Input: A, An array of integers of size n representing a polynomial
        w , a n-root of unity
 Output: [A(w), A(w^2), ..., A(w^(n-1))]
 Complexity: O(n logn)"""
def FFT(A, omega):
    if omega == 1:
        return [sum(A)]
    o2 = omega**2
    C1 = FFT(A[0::2], o2)
    C2 = FFT(A[1::2], o2)
    C3 = [None]*omega.th
    for i in range(omega.th//2):
        C3[i] = C1[i] + omega**i * C2[i]
        C3[i+omega.th//2] = C1[i] - omega**i * C2[i]
    return C3

""" The Fast Polynomial Multiplication Algorithm

 Input: A,B, two arrays of integers representing polynomials
 (coef in increasing deg) their length is in O(n)
 Output: Coefficient representation of AB
 Complexity: O(n logn)"""
def FPM(A,B):
    n = 1<<(len(A)+len(B)-2).bit_length()
    o = NthRootOfUnity(n)
    AT = FFT(A, o)
    BT = FFT(B, o)
    C = [AT[i]*BT[i] for i in range(n)]
    D = [round((a/n).real) for a in FFT(C, o ** -1)]
    while len(D) > 0 and D[-1] == 0:
        del D[-1]
    return D

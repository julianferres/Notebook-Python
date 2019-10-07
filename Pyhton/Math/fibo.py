def matrix_multiplication( A, B):
	"""O(n^3) matrix multiplication"""
	result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*B)]
                                for A_row in A]
	return result

def identity(n):
	"""Matriz identidad de dimension n"""
	return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def matrix_exp( A, n ):
	"""Exponenciacion logaritmica iterativa de matrices,
	A^n, el orden es O(d^3*log n), con d la dimension de la
	matriz"""

	res = identity(len(A))
	while(n>0):
		if(n & 1):
			res = matrix_multiplication(res,A)

		n >>= 1
		A = matrix_multiplication(A, A)

	return res

def fibo_log(n):
    """Returns f_n, using matrix log exponenciation"""
    f = [[0],[1]]
    transition = [[0,1],[1,1]]
    result = matrix_multiplication(matrix_exp(transition,n),f)
    return result[0][0]

"""Could lead to a WA, but O(1) solution (check if **n does not lead to O(n))
"""
def fibo_approx(n):
    phi, phi_conj = (1+5**0.5)/2, (1-5**0.5)/2

    return round((phi**n-phi_conj**n)/(5**0.5))


"""Fast doubling Method"""
def fibo_fast_doubling(n):
    if (n == 0):
        return (0, 1)

    p = fibo_fast_doubling(n >> 1)
    c = p[0]*(2*p[1]- p[0])
    d = p[0]**2 + p[1]**2
    return (d, c + d) if(n & 1) else (c, d)

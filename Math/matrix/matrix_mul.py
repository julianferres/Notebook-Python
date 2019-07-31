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

import timeit

fibo = [[0],[1]]
next = [[0,1],[1,1]]
start1 = timeit.default_timer()
print(matrix_multiplication(matrix_exp(next,10),fibo))
stop1 = timeit.default_timer()

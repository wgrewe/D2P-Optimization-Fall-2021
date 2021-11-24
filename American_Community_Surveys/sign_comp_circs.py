import numpy as  np
def sign_comp_circs(vertex, circuits, B):
	'''
	Input: vertex, set of circuits, constraint matrix B
	Output: set of sign-compatiable circuits to vertex with respect to B
	'''
	sign_comp_circs = []
		for i in circuits:
			if (B.dot(vertex)).dot(transpose(B.dot(i)))>=0:
				sign_comp_circs.append(i)
	return sign_comp_circs
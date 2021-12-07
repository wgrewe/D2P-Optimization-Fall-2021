import numpy as  np
def sign_comp_circs(vertex, circuits,B):
	'''
	Input: vertex, set of circuits, constraint matrix B
	Output: set of sign-compatiable circuits to vertex with respect to B
	'''
	sign_comp_circs = []
	count = 0
	for i in circuits:
		Bu= B.dot(vertex)
		Bg=B.dot(i)
		if (Bu).dot(np.transpose(Bg))>=0:
			vertex_zeros = set(np.where(Bu ==0)[0])
			g_zeros = set(np.where(Bg ==0)[0])
			if vertex_zeros.issubset(g_zeros):
				sign_comp_circs.append(i)
	print('sign_comp finished')
	return sign_comp_circs
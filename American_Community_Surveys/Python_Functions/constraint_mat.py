import numpy as np
def constraint_mat(nodes, clusters):
	'''
	Input: Number of nodes and clusters for the partition polytope
	Output: Constraint matrix for the partition polytope
	'''
	B = np.zeros((clusters,nodes*clusters))

	for i in range(clusters):
		for j in range(nodes):
			B[i,j*clusters+i] = 1

	print('constraint matrix finished')

	return B

import numpy as np
def constraint_mat(nodes, clusters):
	'''
	Input: Number of nodes and clusters for the partition polytope
	Output: Constraint matrix for the partition polytope
	'''
	B = np.zeros((nodes*clusters+clusters,nodes*clusters))

	for i in range(clusters):
		for j in range(nodes):
			B[i,j*clusters+i] = 1

	for i in range(nodes*clusters):
		B[i+clusters,i] = -1

	return B

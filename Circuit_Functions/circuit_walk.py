import numpy as np
import sys as sys

def circuit_walk(vert1,vert2, circuits, B):
	'''
	Input: starting vertex, ending vertex, and a set of sign compatiable circuits with the starting vertex.
	Output: A set of ciruits in roder of their walk from the startin vertex to the ending vertex
	The first for loop picks a sign compatiable circuit from our set. Next we compute all of the lambdas for each component i that could be used in order for our step to match
	one of the vectors in our ending vertex. After these are computed for each compoenntent we keep only the positive values and then pick the smallest one of those. After this
	we update all variables which is the same as taking the step in the circuit walk. 
	'''
	zero = np.zeros(len(vert1))
	end = vert2-vert1
	circ_set = []

	count = 0

	while not np.array_equiv(zero,end):
		B_end = B.dot(end)
		for g in circuits:
			# count += 1

			# if count == len(circuits):
			# 	print('no more circuits to pick')
			# 	print(circ_set)
			# 	sys.exit('Could not Complete Circuit Walk')
			
			# Checking Sign Compatibility
			Bg = B.dot(np.array(np.transpose(np.array(g))))

			sc_check1 = list(filter(lambda c: c < 0, (np.transpose(B_end)*Bg)[0]))
			sc_check2 = list(filter(lambda c: c < 0,(np.transpose(end)*np.transpose(np.array(g)))[0]))
			sc_check = sc_check1+sc_check2
			if not sc_check:
				vertex_zeros = set(np.where(end == 0)[0])
				g_zeros = set(np.where(np.array(g) == 0)[0])
				print('end',np.transpose(end))
				# print('g', g)
				# print('zeros check',vertex_zeros.issubset(g_zeros))
				if vertex_zeros.issubset(g_zeros):
					print('circuit selected and added')
					end -= np.array(g).reshape(len(end),1)
					# print('end:',end)
					circ_set.append(g)
					break

		# Adjustment if not 0/1-polytope
		# for i in range(len(g)):
		# 	if g[i] != 0:
		# 		lamb.append((vert2[i]-s[i])/g[i])
		
		
		# Adjustment if not 0/1-polytope
		# pos_lamb = list(filter(lambda c: c > 0, lamb))
		# # if len(pos_lamb)>0:
		# min_lambda = min(pos_lamb)
		# print('min lamb picked')
		
	print('circ_walk finished')
	return circ_set


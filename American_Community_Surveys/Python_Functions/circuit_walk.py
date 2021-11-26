import numpy as np
def circuit_walk(vert1,vert2, circuits,B):
	'''
	Input: starting vertex, ending vertex, and a set of sign compatiable circuits with the starting vertex.
	Output: A set of ciruits in roder of their walk from the startin vertex to the ending vertex
	The first for loop picks a sign compatiable circuit from our set. Next we compute all of the lambdas for each component i that could be used in order for our step to match
	one of the vectors in our ending vertex. After these are computed for each compoenntent we keep only the positive values and then pick the smallest one of those. After this
	we update all variables which is the same as taking the step in the circuit walk. 
	'''
	s = vert1
	u = vert2-s
	circ_set = []
	picked_circs = []
	lamb = []
	g = 0

	while (any(s != vert2)):
		for i in circuits:
			if list(i) not in picked_circs:
				Bu= B.dot(u)
				Bg=B.dot(i)
				if (Bu).dot(np.transpose(Bg))>0:
					vertex_zeros = set(np.where(Bu == 0)[0])
					g_zeros = set(np.where(Bg == 0)[0])
					if vertex_zeros.issubset(g_zeros):
						g = i
						picked_circs.append(list(g))
						print('g picked')
						break;
		for i in range(len(g)):
			if (g[i] !=0):
				lamb.append((vert2[i]-s[i])/g[i])
		
		print('point g', g)
		print('point s', s)
		print('point u', u)
		print('end vertex', vert2)

		pos_lamb = list(filter(lambda c: c > 0, lamb))
		# if len(pos_lamb)>0:
		min_lambda = min(pos_lamb)
		print('min lamb picked')
		s = s+(min_lambda*g)
		u = vert2-s
		circ_set.append(min_lambda*g)
	print('circ_walk finished')
	return circ_set


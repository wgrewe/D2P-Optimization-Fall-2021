def circuit_walk(vert1,vert2, circuits):
	'''
	Input: starting vertex, ending vertex, and a set of sign compatiable circuits with the starting vertex.
	Output: A set of ciruits in roder of their walk from the startin vertex to the ending vertex
	The first for loop picks a sign compatiable circuit from our set. Next we compute all of the lambdas for each component i that could be used in order for our step to match
	one of the vectors in our ending vertex. After these are computed for each compoenntent we keep only the positive values and then pick the smallest one of those. After this
	we update all variables which is the same as taking teh step in the circuit walk. 
	'''
	s = vert1
	u = vert2-s
	circ_set = []
	picked_circs = []
	lamb = []
	g = 0

	while (s != vert2):
		for i in range(len(circuits)):
			if (circuit[i] not in picked_circs):
				g = circuits[i]
				picked_circs.append(g)
				break;
		for i in range(len(g)):
			if (u[i] != 0):
				lamb.append((s[i]-vert2[i])/g[i])
		
		pos_lamb = list(filter(lambda c: c > 0, lamb))
		min_lambda = min(pos_lamb)

		s = s+min_lamb*g
		u = vert2-s
		circ_set.append(min_lamb*g)

	return circ_set


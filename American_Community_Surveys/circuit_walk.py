def circuit_walk(vert1,vert2, circuits,B):
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


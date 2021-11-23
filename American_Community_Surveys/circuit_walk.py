def circuit_walk(vert1,vert2, circuits,B):
	s = vert1
	u = vert2-s
	circ_set = []
	lamb = []
	g = 0

	while (s != vert2):
		for i in range(len(circuits)):
			if (B.dot(u).dot(B.dot(circuits[i]))>=0):
				g = circuits[i]
				break;
		for i in range(len(g)):
			lamb[i] = (s[i]-vert2[i])/g[i]

		min_lambda = min(lamb)

		s = s+lamb*g
		u = vert2-s
		circ_set.append(lamb*g)

	return circ_set


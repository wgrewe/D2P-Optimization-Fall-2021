def cycles_graph(graph, nodes):
	'''
	input: a graph, and the number of nodes to walk through
	output: all simple cycles paths in the graph 
	logic: use the depth first to find all paths starting at each vertex.
	Use filter to remove walks of length 3 or less since a  simple cycle will need at least 4 vertices at it's smallest.
	Remove all nodes that don't end at a cluster. We end on a cluster when the length of the list of vertices is an even number
	since this corresponds to an odd number of edges. 
	Lastly, add in the start node to the end of each list to represent the cluster node returning to the start node of the cycle. 
	'''
	paths = []
	multi_edge_paths = []
	odd_length_paths = []
	for i in range(nodes):
		visitedList = []
		somePaths = depthFirst(graph, i, [])
		paths += somePaths

	multi_edge_paths = list(filter(lambda c: len(c) >= 3, paths))

	odd_length_paths = list(filter(lambda c: len(c) % 2 == 0 ,multi_edge_paths))
    
	for i in range(len(odd_length_paths)):
		odd_length_paths[i].append(odd_length_paths[i][0])
	return odd_length_paths

	
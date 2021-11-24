import numpy as  np
def build_graph(nodes, clusters):
	'''
	input: number of nodes, number of clusters
	output: complete bipartite graph with vertices labeled 0,..,nodes-1 for 
	elements on the left and nodes,...,clusters-1 for elements on the right
	logic: represent graph as a dictionary, each left node connects to every 
	right node and vice versa. Just fill out dictionary using for-loops
	'''
	graph = {}
	for i in range(nodes):
		graph[i] = [nodes + j for j in range(clusters)]
	for j in range(clusters):
		graph[nodes + j] = [i for i in range(nodes)]
	return graph

# initialize visitedList solely to test depthFirst on its own
visitedList = []
def depthFirst(graph, currentVertex, visited):
    '''
	Input: a graph, a starting vertex, and a list of nodes already visited.
	Typical input should be graph, the starting vertex, and [].
	
	Output: all cycle-free paths in the graph that start with 
	visited + currentVertex
	
	logic: use recursion to find all paths. Start at currentVertex and traverse
	to next vertex if not already visited. When path cant continue, just add to
	visitedList
	'''
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            depthFirst(graph, vertex, visited.copy())
    visitedList.append(visited)
    return visitedList

def cycles_graph(graph, nodes):
	'''
	Input: a graph, and the number of nodes to walk through
	Output: all simple cycles paths in the graph 
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

	multi_edge_paths = list(filter(lambda c: len(c) >= 4, paths))

	even_length_paths = list(filter(lambda c: len(c) % 2 == 0 ,multi_edge_paths))
    
	for i in range(len(even_length_paths)):
		even_length_paths[i].append(even_length_paths[i][0])
	return even_length_paths


def get_cycle_circuits(nodes,clusters):
	graph = build_graph(nodes,clusters)
	cycles = cycles_graph(graph,nodes)

	num_paths = len(cycles)
	circuits = []

	for i in range(num_paths):
		path = paths[i]
		pos_circ = np.zeros(nodes*clusters)

		#Entry (i*C <- number of clusters) + j denotes variable x_ij for i assigned to j

		odd_step = [path[i]*clusters + path[i+1] for i in range(0, len(path)-1, 2)]
		even_step = [path[i]*clusters + path[i+1] for i in range(1, len(path)-1, 2)]

		pos_circ[odd_step] = -1
		pos_circ[even_step] = 1
		neg_circ = -1*pos_circ
		circuits.append(pos_circ)
		circuits.append(neg_circ)
	return circuits
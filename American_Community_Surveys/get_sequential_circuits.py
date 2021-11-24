# Get the sequential path moves

import numpy as np

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
	input: a graph, a starting vertex, and a list of nodes already visited.
	Typical input should be graph, the starting vertex, and [].
	
	output: all cycle-free paths in the graph that start with 
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

def sequential_graph(graph, nodes):
	'''
	input: a graph, and the number of nodes to walk through

	output: all cycle-free paths in the graph 

	logic: use the depth first to find all paths starting at each vertex.
	Use filter to remove all duplicated walks. Since walks are cycle free the
	only way to have a repeat is if the reversed walk was already performed, 
	therefore, repeated walks are those where the end is less than the start.
	Also, filter out all circuits that end on a cluster, these are circuits of 
	odd length.
	'''
	paths = []
	for i in range(nodes):
		visitedList = []
		somePaths = depthFirst(graph, i, [])
		paths += somePaths

	dup_filtered_paths = list(filter(lambda c: c[0] < c[-1], paths))
	even_length_paths = list(filter(lambda c: len(c) % 2 == 0, dup_filtered_paths))

	return even_length_paths

def get_sequential_circuits(nodes, clusters):
	'''
	input: Number of nodes, number of clusters

	output: All sequential circuits for the clustering polyhedron with
	that many nodes and clusters.

	logic: Find all cycle free paths. Transform these paths into circuits
	by labeling 1 if walking into cluster and -1 if walking out of cluster.
	Then add the negative circuit.
	'''
	graph = build_graph(nodes, clusters)
	paths = sequential_graph(graph, nodes)

	num_paths = len(paths)
	circuits = []

	for i in range(num_paths):
		path = paths[i]
		pos_circ = np.zeros(nodes*clusters)
		odd_step = path[::2]
		even_step = path[1::2]
		pos_circ[odd_step] = 1
		pos_circ[even_step] = -1
		neg_circ = -1*pos_circ
		circuits.append(pos_circ)
		circuits.append(neg_circ)

	return circuits
































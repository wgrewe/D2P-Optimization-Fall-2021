# Get the sequential path moves

import numpy as np
import itertools as it

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

def sequential_paths(graph, nodes, clusters):
	'''
	input: a graph, and the number of nodes to walk through

	output: all cycle-free paths in the graph that begin at a cluster

	logic: use the depth first to find all paths starting at each vertex.
	Use filter to remove all duplicated walks. Since walks are cycle free the
	only way to have a repeat is if the reversed walk was already performed, 
	therefore, repeated walks are those where the end is less than the start.
	Also, filter out all circuits that end on a cluster, these are circuits of 
	odd length.
	'''
	paths = []
	for i in range(nodes, nodes+clusters):
		visitedList = []
		somePaths = depthFirst(graph, i, [])
		paths += somePaths

	# filter_dup_paths = list(filter(lambda c: c[0] < c[-1], paths))
	even_length_paths = list(filter(lambda c: len(c) % 2 == 1, paths))
	# paths_set = set(map(tuple,even_length_paths))  #need to convert the inner lists to tuples so they are hashable
	# dup_removed = list(paths_set)
	# final_paths = [list(ele) for ele in dup_removed]

	return even_length_paths

# 5 neighborhoods [0,..,4], 3 clusters [5, 6, 7]
# Path example = [5, 0, 6] <- start on cluster/end on cluster

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
	paths = sequential_paths(graph, nodes, clusters)

	num_paths = len(paths)
	print(num_paths)
	circuits = []

	for path in paths:
		pos_circ = [0]*(nodes*clusters)

		#Entry (i*C <- number of clusters) + j denotes variable x_ij for i assigned to j

		odd_step = [path[i+1]*clusters + (path[i] - nodes) for i in range(0, len(path)-1, 2)]
		even_step = [path[i]*clusters + (path[i+1] - nodes) for i in range(1, len(path)-1, 2)]

		for i in odd_step:
			pos_circ[i] = -1
		for i in even_step:
			pos_circ[i] = 1
		neg_circ = [-1*x for x in pos_circ]

		circuits.append(pos_circ)
		circuits.append(neg_circ)
	print("Finished creating circuits. Now deduplicating.")

	circuits.sort()
	# print('circuits before groupby',circuits)
	print("finished sorting")
	final_circuits = list(k for k,_ in it.groupby(circuits))
	# final_circuits = [np.array(x) for x in final_circuits]
	# print('circuits after groupby',final_circuits)

	# for i in range(num_paths):
	# 	path = paths[i]
	# 	pos_circ = np.zeros(nodes*clusters)

	# 	#Entry (i*C <- number of clusters) + j denotes variable x_ij for i assigned to j

	# 	odd_step = [path[i+1]*clusters + (path[i] - nodes) for i in range(0, len(path)-1, 2)]
	# 	even_step = [path[i]*clusters + (path[i+1] - nodes) for i in range(1, len(path)-1, 2)]

	# 	pos_circ[odd_step] = -1
	# 	pos_circ[even_step] = 1
	# 	neg_circ = -1*pos_circ
	# 	circuits.append(pos_circ)
	# 	circuits.append(neg_circ)

	print("Seq Circuits Finished")
	return final_circuits

































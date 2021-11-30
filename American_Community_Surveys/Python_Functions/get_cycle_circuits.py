import numpy as  np
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
	print("graph built")
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

def cycles_graph(graph, nodes, clusters):
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
	for i in range(clusters-1):
		visitedList = []
		somePaths = depthFirst(graph, nodes+i, [])
		paths+=somePaths
		print("cycles for cluster ", i, "found") 
        
	multi_vertex_paths = list(filter(lambda c: len(c) >= 4, paths))
	even_length_paths = list(filter(lambda c: len(c) % 2 == 0 ,multi_vertex_paths))
	final_cycles = even_length_paths
	# final_cycles = list(set(even_length_paths))
	paths_set = set(map(tuple,even_length_paths))  #need to convert the inner lists to tuples so they are hashable
	dup_removed = list(paths_set)
	final_cycles = [list(ele) for ele in dup_removed]
    
	for cycle in final_cycles:
		cycle.append(cycle[0])  
   
	# print("Graph Cycles Found")
	return final_cycles

def get_cycle_circuits(nodes,clusters):
	graph = build_graph(nodes,clusters)
	print("Graph Built")
	cycles = cycles_graph(graph,nodes, clusters)
	print("Cycles Finished")
	print(len(cycles), " cycles found")
	circuits = []



	for path in cycles:
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
	print("finished sorting")
	final_circuits = list(k for k,_ in it.groupby(circuits))

	# circuits_set = set(map(tuple,circuits))  #need to convert the inner lists to tuples so they are hashable
	# print("converted to set")
	# circ_list = list(paths_set)
	# print("Back to a list of tuples")
	# final_circuits = list(map(list,circ_list))
	print("Cycle Circuits Finished")
	print(len(final_circuits), " total circuits")
	return final_circuits









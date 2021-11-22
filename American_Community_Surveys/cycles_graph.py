def isCircular(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    str1 = ' '.join(map(str, arr1))
    str2 = ' '.join(map(str, arr2))
    if len(str1) != len(str2):
        return False

    return str1 in str2 + ' ' + str2

def cycles_graph(graph, nodes):
	'''
	input: a graph, and the number of nodes to walk through
	output: all simple cycles paths in the graph 
	logic: use the depth first to find all paths starting at each vertex.
	Use filter to remove all duplicated walks. Since walks are cycle free the
	only way to have a repeat is if the reversed walk was already performed, 
	therefore, repeated walks are those where the end is less than the start.
	Also, filter out all circuits that do not end on a cluster, these are circuits of 
	even length.
	'''
	paths = []
	multi_edge_paths = []
	odd_length_paths = []
	for i in range(nodes):
		visitedList = []
		somePaths = depthFirst(graph, i, [])
		paths += somePaths

	multi_edge_paths = list(filter(lambda c: len(c) >= 3, paths))

	odd_length_paths = list(filter(lambda c: c[-1] > nodes ,multi_edge_paths))
    
	for i in range(len(odd_length_paths)):
		odd_length_paths[i].append(odd_length_paths[i][0])
	return odd_length_paths
    
# 	removed_paths = [] 
# 	for i in range(len(odd_length_paths)):
# 		for j in range(len(odd_length_paths)):
# 			if(isCircular(odd_length_paths[i],odd_length_paths[j])):
# 				removed_paths.append(odd_length_paths[i])
                
# 	for i in range(len(removed_paths)):
# 		if removed_paths[i] in odd_length_paths:
# 			odd_length_paths.remove(removed_paths[i])

	
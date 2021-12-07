import numpy as np 
import itertools as it

def filter_by_zeros(vertex_diff, circuits):
	'''
	input: vertex <array float> the ending vertex of circuit walk.
	circuits <array float> the set of circuits for the problem.

	output: sc_circuits <array float> the set of circuits that 
	have a zero wherever vertex has a zero

	logic: use np.where to extract indices of vertex zeros and then 
	for each circuit use np.where to extract indices of circuit zeros.
	If vertex zeros are a subset of circ zeros add them to the list of 
	circuits to be returned (sc_circuits)
	'''
	if isinstance(circuits, np.ndarray):
		circuits = list(circuits)
	if isinstance(vertex_diff, list):
		vertex_diff = np.array(vertex_diff)

	vertex_zeros = set(np.where(vertex_diff == 0)[0]) # indices of vertex zeros
	sc_circuits = []
	for circuit in circuits:
		if isinstance(circuit, list):
			circuit = np.array(circuit)
		circ_zeros = set(np.where(circuit == 0)[0])
		if vertex_zeros.issubset(circ_zeros):
			sc_circuits.append(circuit)
	print('filter by zeros finished', len(np.array(sc_circuits)))
	return np.array(sc_circuits)

def sort_circuits(circuits, dist):
	'''
	input: circuits <list list float / array float> the list of circuits
	dist <list float> an associated list of distance values for each circuit

	output: the circuits after being sorted by distance

	logic:
	'''
	if isinstance(circuits, np.ndarray):
		circuits = list(circuits)

	sorted_with_dists = sorted(zip(circuits, dist),key=lambda x: x[1])
	sorted_circs = np.array([x[0] for x in sorted_with_dists])
	print('Circuits Have Been Sorted')
	print('New Total Number of Circuits', len(sorted_circs))
	return sorted_circs

def neighbor_indices(circuit, num_clusters):
	'''
	input: circuit <array>, num_clusters <int> is the number of clusters 

	output: the IDs of neighbors changed by the circuit (currently only works
	for clustering problems)

	logic: Use np.where to extract indices of neighborhoods being changed.
	int-div by num_clusters to get the neighborhood id
	'''

	active_neighbors = np.where(circuit == 1)[0]
	neighbor_id = active_neighbors // num_clusters
	return neighbor_id

def get_circuit_dist(circuit, dist_mat, num_clusters, max_dist):
	'''
	input: circuit <array/list>, dist_mat <list list size num_nodes x num_nodes>
	contains the distances between the neighborhoods
	num_clusters <float> the number of clusters. max_dist <float> is what to assign
	when just one node is reassigned [ideally 2*max(max_dist)] 

	output: the minimum distance of all the distances computed

	logic: find indices for each active neighborhood. For every pair for neighborhoods
	compute their distance. Then take the minimum of these distances
	'''
	if isinstance(circuit, list):
		circuit = np.array(circuit)

	indices = neighbor_indices(circuit, num_clusters)

	if len(indices) == 1:
		return 2*max_dist

	candidate_dist = []
	for pair in it.combinations(indices,2):
		dist = dist_mat[pair[0],pair[1]]
		candidate_dist.append(dist)

	dist = min(candidate_dist)
	return dist

def get_all_circuit_dists(circuits, dist_mat, num_clusters, max_dist):
	'''
	input: circuits <array/list list> of all the circuits 
	dist_mat <list list size num_nodes x num_nodes>
	contains the distances between the neighborhoods
	num_clusters <float> the number of clusters. max_dist <float> is what to assign
	when just one node is reassigned [ideally 2*max(max_dist)] 

	output: dists <list float> the minimum distance computed for each circuit.

	logic: Just a list comprehension. Broken up from get_circuit_dist for easier 
	debugging/testing matters
	'''
	if isinstance(circuits, np.ndarray):
		circuits = list(circuits)
	dists = [get_circuit_dist(circ, dist_mat, num_clusters, max_dist) for circ in circuits]
	return dists



















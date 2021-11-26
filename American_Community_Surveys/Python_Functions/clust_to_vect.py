def cluster_to_vector(cluster_assign, num_clusters):
	num_nodes = len(cluster)
	cluster = np.array(cluster)


	binary_assignments = np.zeros((num_nodes, num_clusters))
	for i in range(num_nodes):
		binary_assignments[i, cluster[i]] = 1

	return binary_assignments
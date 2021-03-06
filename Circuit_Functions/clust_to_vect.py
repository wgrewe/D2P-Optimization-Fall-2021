import numpy as np
def cluster_to_vector(cluster_assign, num_clusters):
	num_nodes = len(cluster_assign)
	cluster = np.array(cluster_assign)


	binary_assignments = np.zeros((num_nodes, num_clusters))
	for i in range(num_nodes):
		binary_assignments[i, cluster[i]] = 1

	correct_vec =np.reshape(binary_assignments,(1,num_nodes*num_clusters)) 	

	return correct_vec
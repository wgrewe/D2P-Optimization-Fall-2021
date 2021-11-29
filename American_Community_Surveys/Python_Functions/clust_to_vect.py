import numpy as np
def cluster_to_vector(cluster_assign, num_clusters):
	num_nodes = len(cluster_assign)
	cluster = np.array(cluster_assign)


	binary_assignments = np.zeros((num_nodes, num_clusters))
	for i in range(num_nodes):
		binary_assignments[i, cluster[i]-1] = 1

	correct_vec =np.reshape(binary_assignments,(num_nodes*num_clusters,1)) 	

	return correct_vec

# nodes = 3

# cluster_ass = np.array([1,2,1,3,1,1,2,3,3,2])

# clust_vect = cluster_to_vector(cluster_ass,nodes)
# print(len(clust_vect))
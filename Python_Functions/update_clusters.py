import numpy as np

def update_clusters(cluster, circuit):
	'''
	input: a set of cluster labels <list float> C where c_i in {1,..., k}.
	a circuit <list float> for the cluster polyhedron

	output: the updated set of clusters after walking in the direction of the circuit
	
	logic: cluster numbers are assigned for each nodes, so num_nodes is len(cluster)
	circuit length is num_clusters*num_nodes, so division return num_clusters

	Transform cluster assignment to binary matrix where [i,j] = 1 if elt i is assigned
	to cluster j and 0 otherwise. Then reshape so it may be broadcasted with the circuit

	Transform back to a list of cluster labels.
	'''

	num_nodes = len(cluster)
	cluster = np.array(cluster)
	num_clusters = len(circuit)//num_nodes


	binary_assignments = np.zeros((num_nodes, num_clusters))
	for i in range(num_nodes):
		binary_assignments[i, cluster[i]] = 1

	binary_assignments = np.reshape(binary_assignments, num_clusters*num_nodes)

	updated = list(binary_assignments + circuit)
	print(updated)
	print(updated[num_clusters*0:num_clusters*(0+1)].index(1))

	new_cluster_labels = [updated[num_clusters*i:num_clusters*(i+1)].index(1) 
		for i in range(num_nodes)]

	return new_cluster_labels 

def cluster_to_circuit(cluster, num_clusters):
	circuit = np.zeros(len(cluster)*num_clusters)
	
	for i in range(len(cluster)):
		circuit[(i*num_clusters)+cluster[i]] = 1

	return circuit



def circuit_to_cluster(circuit, num_nodes):
	'''
	input: A circuit <list int>, the number of neighborhoods/nodes etc.

	output: A label for each neighborhood of -1, 0, 1 if its 
	cluster rank is decreasing, stagnant, or increasing. 
	Makes sense if cluster 0 is the least privileged cluster and 
	cluster K is the most-privileged cluster. Then can be used for plotting
	with the plot_clusters function
	'''

	labels = np.zeros(num_nodes)
	
	num_clusters = len(circuit)//num_nodes
	for i in range(num_nodes):
		if 1 in circuit[i*num_clusters:(i+1)*num_clusters]:
			if circuit[i*num_clusters:(i+1)*num_clusters].index(1) < circuit[i*num_clusters:(i+1)*num_clusters].index(-1):
				labels[i] = -1
			else:
				labels[i] = 1

	return labels


def plot_clusters(dataset, clusters, shapefile, title = "Plot of Clusters"):
	'''
	Input: dataset: <pandas dataframe> with columns NBHD_ID, NBHD_NAME.
	Clusters: <list> a set of cluster labels for the neighborhoods, must be 
	in the same order as the neighborhoods in the dataset.
	Shapefile: A shapefile (give filepath with .shx, all other links should be
	in the same folder) to plot data, should have column of NBHD_ID to be
	merged on.
	Title: Give it a title if you want

	Output: A map with the clusters plotted that includes a legend.

	Logic: Updates the dataset with the cluster labels, then plots the data.

	Required packages
	'''
	
	dataset.assign(CLUSTER=clusters)
	clusters = dataset[["NBHD_NAME", "CLUSTER"]]

	map_df = gpd.read_file(shapefile)

	plot = map_df.merge(dataset, left_on=["NBHD_ID"], right_on=["NBHD_ID"])

	fig, ax = plt.subplots(1, figsize=(10,6))
	plot.plot(column='CLUSTER', cmap='Blues', linewidth=1, ax=ax, edgecolor='0.9', legend = True)
	ax.axis('off')
	fig.suptitle(title, fontsize=16)





































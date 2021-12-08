import numpy as np
import itertools as it
import pandas as pd
import constraint_mat as cm
import sign_comp_circs as scc
import circuit_walk as cw
import get_sequential_circuits as gsc
import get_cycle_circuits as gcc
import clust_to_vect as ctv
from numpy import savetxt
import implement_geographic_distance as igd

# ###import cluster assignments from a CSV
cluster_06 = np.array(pd.read_csv("https://raw.githubusercontent.com/wgrewe/D2P-Optimization-Fall-2021/main/Data/2006_clusters.csv", header = None)).astype(int)
cluster_10 = np.array(pd.read_csv("https://raw.githubusercontent.com/wgrewe/D2P-Optimization-Fall-2021/main/Data/2010_clusters.csv", header = None)).astype(int)
cluster_15 = np.array(pd.read_csv("https://raw.githubusercontent.com/wgrewe/D2P-Optimization-Fall-2021/main/Data/2015_clusters.csv", header = None)).astype(int)

clusters = 3
nodes = len(cluster_06)
visitedList= []
circuits = []

# ##convert cluster assignments to vectors in the polyhedron space
vert_06 = np.transpose(ctv.cluster_to_vector(cluster_06,clusters))
vert_10 = np.transpose(ctv.cluster_to_vector(cluster_10,clusters))
vert_15 = np.transpose(ctv.cluster_to_vector(cluster_15,clusters))

# ### import distance matrices from CSV and conver to np.arrays
dist_mat_06 = np.array(pd.read_csv("https://raw.githubusercontent.com/wgrewe/D2P-Optimization-Fall-2021/main/Data/dist_mat_2006.csv", header = None))
dist_mat_10 = np.array(pd.read_csv("https://raw.githubusercontent.com/wgrewe/D2P-Optimization-Fall-2021/main/Data/dist_mat_2006.csv", header = None))
dist_mat_15 = np.array(pd.read_csv("https://raw.githubusercontent.com/wgrewe/D2P-Optimization-Fall-2021/main/Data/dist_mat_2006.csv", header = None))

###test case
# vert1 = np.array([1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1])
# vert2 = np.array([1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0])
# nodes = 6


def main(nodes,clusters,vert1,vert2):
	### getting circuits
	seq_circuits = gsc.get_sequential_circuits(nodes,clusters)
	graph = gcc.build_graph(nodes, clusters)
	cyc_circuits = gcc.get_cycle_circuits(nodes, clusters)
	circuits = seq_circuits+cyc_circuits
	print('total number of circuits', len(circuits))
	### performing circuit walk
	B = cm.constraint_mat(nodes,clusters)
	circ_walk = cw.circuit_walk(vert1,vert2,circuits,B)

	print(len(circ_walk))
	return circ_walk

def main_geo(nodes,clusters,vert1,vert2, dist_mat, max_dist):
	### getting circuits
	seq_circuits = gsc.get_sequential_circuits(nodes,clusters)
	graph = gcc.build_graph(nodes, clusters)
	cyc_circuits = gcc.get_cycle_circuits(nodes, clusters)
	circuits = seq_circuits+cyc_circuits
	print('total number of circuits', len(circuits))
		###sorting circuits by distance###
	no_zeros = igd.filter_by_zeros(vert2-vert1,circuits)
	circ_distances = igd.get_all_circuit_dists(no_zeros, dist_mat, clusters, max_dist)
	sorted_circs = igd.sort_circuits(no_zeros, circ_distances)
	print('circuits sorted finished')
	print('Total number of sorted circuits',len(sorted_circs))

	### performing circuit walk
	B = cm.constraint_mat(nodes,clusters)
	circ_walk = cw.circuit_walk(vert1,vert2,sorted_circs,B)

	print(len(circ_walk))
	return circ_walk

	
if __name__ == '__main__':
	# ### Without Geogrpahic Info ###
	# circ_06_to_10 =main(nodes,clusters,vert_06,vert_10)
	# circ_10_to_15 =main(nodes,clusters,vert_10,vert_15)
	# circ_06_to_15 =main(nodes,clusters,vert_06,vert_15)

	# #save walks
	# savetxt('2006_to_2010_circuitwalk.csv',circ_06_to_10,delimiter = ',')
	# savetxt('2010_to_2015_circuitwalk.csv',circ_10_to_15,delimiter = ',')
	# savetxt('2006_to_2015_circuitwalk.csv',circ_06_to_15,delimiter = ',')

	### With Geogrpahic Info ###
	max_dist = dist_mat_06.max()
	circ_06_to_10_geo =main_geo(nodes,clusters,vert_06,vert_10, dist_mat_06, max_dist)
	max_dist = dist_mat_10.max()
	circ_10_to_15_geo =main_geo(nodes,clusters,vert_10,vert_15, dist_mat_10, max_dist)
	max_dist = dist_mat_15.max()
	circ_06_to_15_geo =main_geo(nodes,clusters,vert_06,vert_15, dist_mat_15, max_dist)

	#save walks
	savetxt('2006_to_2010_circuitwalk_geo.csv',circ_06_to_10_geo,delimiter = ',')
	savetxt('2010_to_2015_circuitwalk_geo.csv',circ_10_to_15_geo,delimiter = ',')
	savetxt('2006_to_2015_circuitwalk_geo.csv',circ_06_to_15_geo,delimiter = ',')
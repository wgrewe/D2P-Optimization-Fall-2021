import numpy as np
import pandas as pd
import constraint_mat as cm
import sign_comp_circs as scc
import circuit_walk as cw
import get_sequential_circuits as gsc
import get_cycle_circuits as gcc
import clust_to_vect as ctv


nodes = 78
clusters = 3
visitedList= []
circuits = []
# ###import cluster assignments from a CSV
cluster_06 = np.array(pd.read_csv('2006_clsuters.csv')).astype(int)
cluster_10 = np.array(pd.read_csv('2010_clusters.csv')).astype(int)
cluster_15 =  np.array(pd.read_csv('2015_clusters.csv')).astype(int)
# ##convert cluster assignments to vectors in the polyhedron space
vert_06 = ctv.cluster_to_vector(cluster_06,clusters)
vert_10 = ctv.cluster_to_vector(cluster_10,clusters)
vert_15 = ctv.cluster_to_vector(cluster_15,clusters)

# vert1 = np.array([1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1])
# vert2 = np.array([1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0])
vert1 = vert_06
vert2 = vert_10

def main(nodes,clusters,vert1,vert2):
	seq_circuits = gsc.get_sequential_circuits(nodes,clusters)
	cyc_circuits = gcc.get_cycle_circuits(nodes,clusters)
	circuits = seq_circuits+cyc_circuits
	B = cm.constraint_mat(nodes,clusters)
	circ_walk = cw.circuit_walk(vert1,vert2,circuits,B)
	print(len(circ_walk))
	print(circ_walk)
	return circ_walk


if __name__ == '__main__':
	main(nodes,clusters,vert1,vert2)



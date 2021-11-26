import numpy as np
# import pandas as pd
import constraint_mat as cm
import sign_comp_circs as scc
import circuit_walk as cw
import get_sequential_circuits as gsc
import get_cycle_circuits as gcc
# import clust_to_vert as ctv


nodes = 6
clusters = 3
visitedList= []
circuits = []
# ###import cluster assignments from a CSV
# 2006_clust = pd.read_csv()
# 2010_clust = pd.read_csv()
# 2015_clust =  pd.read_csv()
# ##convert cluster assignments to vectors in the polyhedron space
# 2006_vert = ctv.cluster_to_vector(2006_clust,clusters)
# 2010_vert = ctv.cluster_to_vector(2010_clust,clusters)
# 2015_vert = ctv.cluster_to_vector(2015_clust,clusters)

vert1 = np.array([1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1])
vert2 = np.array([1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0])

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



import numpy as np
import constraint_mat
import sign_comp_circs
import circuit_walk
import cycles_graph
import get_sequential_circuits

nodes = 5
clusters = 3
visitedList= []
vert1 = [0,0,1,0,1,0,1,0,0,0,0,1,0,1,0]
vert2 = [0,0,1,1,0,0,1,0,0,1,0,0,0,1,0]

def main(nodes,clusters,vert1,vert2):
	graph = build_graph(nodes,clusters)
	cyc_graph = cycles_graph(graph,nodes)
	circuits = get_sequential_circuits(nodes,clusters)
	#make one for cycles#
	B = constraint_mat(nodes,clusters)
	sign_comp = sign_comp_circs(vert2-vert1,circuits,B)
	circ_walk = circuit_walk(vert1,vert2,sign_comp)
	return circ_walk


if __name__ == '__main__':
	main(nodes,clusters)


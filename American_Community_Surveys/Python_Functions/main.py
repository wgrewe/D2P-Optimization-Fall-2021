import numpy as np
import constraint_mat as cm
import sign_comp_circs as scc
import circuit_walk as cw
import cycles_graph as cg
import get_sequential_circuits as gsc

nodes = 5
clusters = 3
visitedList= []
vert1 = [0,0,1,0,1,0,1,0,0,0,0,1,0,1,0]
vert2 = [0,0,1,1,0,0,1,0,0,1,0,0,0,1,0]

def main(nodes,clusters,vert1,vert2):
	graph = gsc.build_graph(nodes,clusters)
	cyc_graph = cg.cycles_graph(graph,nodes)
	circuits = gsc.get_sequential_circuits(nodes,clusters)
	#make one for cycles#
	B = cm.constraint_mat(nodes,clusters)
	sign_comp = scc.sign_comp_circs(vert2-vert1,circuits,B)
	circ_walk = cw.circuit_walk(vert1,vert2,sign_comp)
	return circ_walk


if __name__ == '__main__':
	main(nodes,clusters,vert1,vert2)


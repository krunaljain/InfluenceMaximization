#!/usr/local/bin/python3.6

import sys, random
from Graph import *
from ReadDataset import *
sys.setrecursionlimit(100000)
import time;



# random.seed(0)

def main () :
    edges_list, weight_list, nodes_set = ReadGraphFile (sys.argv[1])
    graph_snaps = CreateRandomGraphs (50, edges_list, weight_list)

    # for graph in graph_snaps :
    #     print ("new graph")
    #     graph.print_graph ()
    # y = []
    # for i in range (1,10) :
    #     l = len((find_influence (set([24325]), graph_snaps, i)))
    #     print (l)
    #     y.append(l)
    
    # np.plot (range (1,10), y)
    # np.show ()
    
    # i = 0
    # nodes_list = list(nodes_set)
    # for i in range(len(nodes_list)-10) :
    #     # print (i, len(find_influence (set([nodes_list[i], nodes_list[i+1], nodes_list[i+2], nodes_list[i+3], nodes_list[i+4]]), graph_snaps, 45)))
    #     print (i, nodes_list[i], len(find_influence (set([nodes_list[i]]), graph_snaps, 30)))

    


main ()

#!/usr/bin/env python
# coding: utf-8

import pickle
import networkx as nx
from graph_utils import *
import numpy as np
import igraph as ig



def main():

    
    
    print ("CBOW")
    with open('/home/fgazzavi/f_env/Thai/CBOW/Thai_Gabriel_Graph_sample1%_CBOW_1gram_6.pkl', 'rb') as inp:
        At_graph_cbow_1g6 = pickle.load(inp)

    gabriel = At_graph_cbow_1g6.get_networkx_graph()
    graph = ig.Graph.from_networkx(gabriel)

    with open('/home/fgazzavi/f_env/Thai/CBOW/Thai_Gabriel_Graph_sample1%_CBOW_1gram_6_ig.pkl', 'wb') as outp:
        pickle.dump(graph, outp, pickle.HIGHEST_PROTOCOL)
        
    wd = graph.diameter(weights="weight")
    awsp = np.mean(graph.shortest_paths(weights="weight"))
    with open('/home/fgazzavi/f_env/Thai/CBOW/Diamter_CBOW.txt', 'a',encoding='utf-8') as f:
        f.write(f"CBOW diameter is : {graph.diameter()}\n")
        f.write(f"CBOW radius is :{graph.radius()}\n")
        f.write(f"Average Shortest paths is : {np.mean(graph.shortest_paths())}\n")
        f.write(f"CBOW Number of edges:{graph.ecount()}\n")
        f.write(f"CBOW Number of vertices:{graph.vcount()}\n")
        f.write(f"CBOW CC (clustering coefficient) is :{graph.transitivity_undirected()}\n")
        f.write(f"CBOW ACC (Average clustering coefficient) is :{graph.transitivity_avglocal_undirected()}\n")
        f.write(f"CBOW Degree Assortativity is :{graph.assortativity_degree()}\n")
        f.write(f"CBOW weighted diameter is : {wd}\n")
        f.write(f"CBOW Average weighted Shortest paths is : {awsp}\n")

    names = []
    for v in graph.vs:
        names.append(v['_nx_name'])

    degree = graph.degree()
    degree_dic= {}
    for key,value in zip(names, degree):
        degree_dic[key] = value
    print(degree_dic)
    with open('/home/fgazzavi/f_env/Thai/CBOW/Thai_degree_CBOW_1gram_6_ig.pkl', 'wb') as outp:
        pickle.dump(degree_dic, outp, pickle.HIGHEST_PROTOCOL)

    cc = graph.closeness(weights="weight")
    cc_dic_w = {}
    for key,value in zip(names, cc):
        cc_dic_w[key] = value
    print(cc_dic_w)
    with open('/home/fgazzavi/f_env/Thai/CBOW/Thai_CCW_CBOW_1gram_6_ig.pkl', 'wb') as outp:
        pickle.dump(cc_dic_w, outp, pickle.HIGHEST_PROTOCOL)

    cc = graph.closeness()
    cc_dic= {}
    for key,value in zip(names, cc):
        cc_dic[key] = value
    print(cc_dic)
    with open('/home/fgazzavi/f_env/Thai/CBOW/Thai_CC_CBOW_1gram_6_ig.pkl', 'wb') as outp:
        pickle.dump(cc_dic, outp, pickle.HIGHEST_PROTOCOL)

    bc = graph.betweenness()
    bc_dic= {}
    for key,value in zip(names, bc):
        bc_dic[key] = value
    print(bc_dic)
    with open('/home/fgazzavi/f_env/Thai/CBOW/Thai_BC_CBOW_1gram_6_ig.pkl', 'wb') as outp:
        pickle.dump(bc_dic, outp, pickle.HIGHEST_PROTOCOL)

    bc = graph.betweenness(weights="weight")
    bc_dic_w= {}
    for key,value in zip(names, bc):
        bc_dic_w[key] = value
    print(bc_dic_w)
    with open('/home/fgazzavi/f_env/Thai/CBOW/Thai_BCW_CBOW_1gram_6_ig.pkl', 'wb') as outp:
        pickle.dump(bc_dic_w, outp, pickle.HIGHEST_PROTOCOL)

    


   
if __name__ == "__main__":

    main()




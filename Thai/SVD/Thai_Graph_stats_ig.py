#!/usr/bin/env python
# coding: utf-8

import pickle
from stats_utils import *
import numpy as np
import matplotlib.pyplot as plt


def main():

    print ("SVD")
    
    with open('/home/fgazzavi/f_env/Thai/SVD/Thai_Gabriel_Graph_sample1%_SVD_1gram_6_ig.pkl', 'rb') as inp:
        graph = pickle.load(inp)

    weights = []
    for e in graph.es:
        weights.append(e['weight'])
    print (max(weights))
    diameter = max(weights) +1
    #diameter = 40
    limit = 500
    human, bot = return_Arrays_of_path_length_withNFAndLimit( "/home/fgazzavi/f_env/Thai/SVD/test_original_corpus_SVD.txt", "/home/fgazzavi/f_env/Thai/SVD/test_bot_corpus_SVD.txt",graph,diameter,limit)
    X = np.arange(0,len(human))
    plt.plot(X, human, color='r', label='human')
    plt.plot(X, bot, color='g', label='bot')
    plt.xlabel("text number")
    plt.ylabel("Weighted Path length")
    plt.title("Weighted path length for texts generated by humans and bots")
    plt.legend()
    plt.savefig('/home/fgazzavi/f_env/Thai/SVD/Thai_Weighted_path_length_SVD_500.pdf')
    #plt.show()

    plt.clf()


    with open('/home/fgazzavi/f_env/Thai/SVD/Thai_CCW_SVD_1gram_6_ig.pkl', 'rb') as outp:
        cc_dic = pickle.load(outp)
    human , bot = return_Arrys_of_centralites( "/home/fgazzavi/f_env/Thai/SVD/test_original_corpus_SVD.txt", "/home/fgazzavi/f_env/Thai/SVD/test_bot_corpus_SVD.txt",graph,cc_dic,limit)
    X = np.arange(0,len(human))
    plt.plot(X, human, color='r', label='human')
    plt.plot(X, bot, color='g', label='bot')
    plt.xlabel("text number")
    plt.ylabel("Weighted closness centrality")
    plt.title("Weighted closness Centrality for texts generated by humans and bots")
    plt.legend()
    plt.savefig('/home/fgazzavi/f_env/Thai/SVD/Thai_Weighted_cc_SVD_500.pdf')

    plt.clf()

    with open('/home/fgazzavi/f_env/Thai/SVD/Thai_BCW_SVD_1gram_6_ig.pkl', 'rb') as outp:
        bc_dic = pickle.load(outp)
    human , bot = return_Arrys_of_centralites("/home/fgazzavi/f_env/Thai/SVD/test_original_corpus_SVD.txt", "/home/fgazzavi/f_env/Thai/SVD/test_bot_corpus_SVD.txt",graph,bc_dic,limit)
    X = np.arange(0,len(human))
    plt.plot(X, human, color='r', label='human')
    plt.plot(X, bot, color='g', label='bot')
    plt.xlabel("text number")
    plt.ylabel("Weighted betweeness centrality")
    plt.title("Weighted betweeness centrality for texts generated by humans and bots")
    plt.legend()
    plt.savefig('/home/fgazzavi/f_env/Thai/SVD/Thai_Weighted_bc_SVD_500.pdf')

    plt.clf()
   
if __name__ == "__main__":

    main()




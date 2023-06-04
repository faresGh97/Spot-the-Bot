#!/usr/bin/env python
# coding: utf-8

import pickle
from stats_utils import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon


def main():

    print ("CBOW")
    
    with open('/home/fgazzavi/f_env/English/English_nk/English_Gabriel_Graph_sample1%_CBOW_1gram_6_ig.pkl', 'rb') as inp:
        graph = pickle.load(inp)

    weights = []
    for e in graph.es:
        weights.append(e['weight'])
    print (max(weights))
    diameter = max(weights) +1
    limit = 500
    human, bot = return_Arrays_of_path_length_withNFAndLimit( "/home/fgazzavi/f_env/English/English_nk/test_original_corpus_CBOW_modified.txt", "/home/fgazzavi/f_env/English/English_nk/test_bot_corpus_CBOW.txt",graph,diameter,limit)
    
    with open('/home/fgazzavi/f_env/English/English_nk/wilcoxon_CBOW.txt', 'a',encoding='utf-8') as f:
        f.write(f"Wilcoxon Signed-Rank Test for human and bots samples (Path length)\n")
        stat, p = wilcoxon(human, bot)
        f.write('Statistics=%.3f, p=%.3f \n' % (stat, p))
        alpha = 0.05
        if p > alpha:
            f.write(f"Same distribution (fail to reject H0)\n")
        else:
            f.write(f"Different distribution (reject H0)\n")

    with open('/home/fgazzavi/f_env/English/English_nk/English_CCW_CBOW_1gram_6_ig.pkl', 'rb') as outp:
        cc_dic = pickle.load(outp)
    human , bot = return_Arrys_of_centralites( "/home/fgazzavi/f_env/English/English_nk/test_original_corpus_CBOW_modified.txt", "/home/fgazzavi/f_env/English/English_nk/test_bot_corpus_CBOW.txt",graph,cc_dic,limit)
    with open('/home/fgazzavi/f_env/English/English_nk/wilcoxon_CBOW.txt', 'a',encoding='utf-8') as f:
        f.write(f"Wilcoxon Signed-Rank Test for human and bots samples (Closness centrality)\n")
        stat, p = wilcoxon(human, bot)
        f.write('Statistics=%.3f, p=%.3f \n' % (stat, p))
        alpha = 0.05
        if p > alpha:
            f.write(f"Same distribution (fail to reject H0)\n")
        else:
            f.write(f"Different distribution (reject H0)\n")

    with open('/home/fgazzavi/f_env/English/English_nk/English_BCW_CBOW_1gram_6_ig.pkl', 'rb') as outp:
        bc_dic = pickle.load(outp)
    human , bot = return_Arrys_of_centralites("/home/fgazzavi/f_env/English/English_nk/test_original_corpus_CBOW_modified.txt", "/home/fgazzavi/f_env/English/English_nk/test_bot_corpus_CBOW.txt",graph,bc_dic,limit)
    with open('/home/fgazzavi/f_env/English/English_nk/wilcoxon_CBOW.txt', 'a',encoding='utf-8') as f:
        f.write(f"Wilcoxon Signed-Rank Test for human and bots samples (Betweeness centrality)\n")
        stat, p = wilcoxon(human, bot)
        f.write('Statistics=%.3f, p=%.3f \n' % (stat, p))
        alpha = 0.05
        if p > alpha:
            f.write(f"Same distribution (fail to reject H0)\n")
        else:
            f.write(f"Different distribution (reject H0)\n")

    print ("SVD")
    
    with open('/home/fgazzavi/f_env/English/English_nk/English_Gabriel_Graph_sample1%_SVD_1gram_6_ig.pkl', 'rb') as inp:
        graph = pickle.load(inp)

    weights = []
    for e in graph.es:
        weights.append(e['weight'])
    print (max(weights))
    diameter = max(weights) +1
    limit = 500
    human, bot = return_Arrays_of_path_length_withNFAndLimit( "/home/fgazzavi/f_env/English/English_nk/test_original_corpus_SVD_modified.txt", "/home/fgazzavi/f_env/English/English_nk/test_bot_corpus_SVD.txt",graph,diameter,limit)
    with open('/home/fgazzavi/f_env/English/English_nk/wilcoxon_SVD.txt', 'a',encoding='utf-8') as f:
        f.write(f"Wilcoxon Signed-Rank Test for human and bots samples (Path length)\n")
        stat, p = wilcoxon(human, bot)
        f.write('Statistics=%.3f, p=%.3f \n' % (stat, p))
        alpha = 0.05
        if p > alpha:
            f.write(f"Same distribution (fail to reject H0)\n")
        else:
            f.write(f"Different distribution (reject H0)\n")


    with open('/home/fgazzavi/f_env/English/English_nk/English_CCW_SVD_1gram_6_ig.pkl', 'rb') as outp:
        cc_dic = pickle.load(outp)
    human , bot = return_Arrys_of_centralites( "/home/fgazzavi/f_env/English/English_nk/test_original_corpus_SVD_modified.txt", "/home/fgazzavi/f_env/English/English_nk/test_bot_corpus_SVD.txt",graph,cc_dic,limit)
    with open('/home/fgazzavi/f_env/English/English_nk/wilcoxon_SVD.txt', 'a',encoding='utf-8') as f:
        f.write(f"Wilcoxon Signed-Rank Test for human and bots samples (Closness centrality)\n")
        stat, p = wilcoxon(human, bot)
        f.write('Statistics=%.3f, p=%.3f \n' % (stat, p))
        alpha = 0.05
        if p > alpha:
            f.write(f"Same distribution (fail to reject H0)\n")
        else:
            f.write(f"Different distribution (reject H0)\n")

    with open('/home/fgazzavi/f_env/English/English_nk/English_BCW_SVD_1gram_6_ig.pkl', 'rb') as outp:
        bc_dic = pickle.load(outp)
    human , bot = return_Arrys_of_centralites("/home/fgazzavi/f_env/English/English_nk/test_original_corpus_SVD_modified.txt", "/home/fgazzavi/f_env/English/English_nk/test_bot_corpus_SVD.txt",graph,bc_dic,limit)
    with open('/home/fgazzavi/f_env/English/English_nk/wilcoxon_SVD.txt', 'a',encoding='utf-8') as f:
        f.write(f"Wilcoxon Signed-Rank Test for human and bots samples (Betweeness centrality)\n")
        stat, p = wilcoxon(human, bot)
        f.write('Statistics=%.3f, p=%.3f \n' % (stat, p))
        alpha = 0.05
        if p > alpha:
            f.write(f"Same distribution (fail to reject H0)\n")
        else:
            f.write(f"Different distribution (reject H0)\n")
   
if __name__ == "__main__":

    main()




#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse.linalg import svds
from IPython.display import clear_output
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
import pickle
import io 
import json
from gensim.models import Word2Vec
from graph_utils import *


def main():

    print ("SVD")

    At_VECTORIZED_CORPUS = "/home/fgazzavi/f_env/Thai/SVD/Thai_vectorized_corpus_sample1%_SVD_1gram_6.npy"
    at_corpus = np.load(At_VECTORIZED_CORPUS, allow_pickle=True)
    at_corpus = at_corpus.tolist()

    vertices = create_vertices(at_corpus, 6)

    gg = GG(vertices)
    print ("start deluany")
    gg.create_delaunay_graph()
    print ("finished delauny")
    with open('/home/fgazzavi/f_env/Thai/SVD/Thai_Delauny_Graph_sample1%_SVD_1gram_6.pkl', 'wb') as outp:
        pickle.dump(gg, outp, pickle.HIGHEST_PROTOCOL)
    print("start pgg")
    gg.create_parallel_gabriel_graph(gg.triangles,10)
    print ("end pgg ")
    
    with open('/home/fgazzavi/f_env/Thai/SVD/Thai_Gabriel_Graph_sample1%_SVD_1gram_6.pkl', 'wb') as outp:
        pickle.dump(gg, outp, pickle.HIGHEST_PROTOCOL)

   
if __name__ == "__main__":

    main()
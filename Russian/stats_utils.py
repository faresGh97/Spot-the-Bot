import networkx as nx
from tqdm import tqdm
import numpy as np
import igraph as ig


def go_through_text_with_NF(text: str, graph: ig.Graph, nodes: list) -> list:
    '''
    Convert text to path on igraph graph

    Parameters
    ----------
    text: str
    graph: nx.classes.graph.Graph

    Returns
    -------
    path_edges : list

    text = "word_1 word_2 ... word_n"
    Shortest path from word_i to word_i+1 is nx.dijkstra_path(graph, word_i, word_i+1)
    Shortest paths through text [(word_1, word_1_1, word_1_2, ..., word_1_n, word_2),
                                 (word_2, ..., word_3),
                                 (word_3, ..., word_4) ..., (word_n-1, ..., word_n)]
    '''
    text = text.split()
    path_edges = []
    current_word = text[0]
    file_ = open("Ar_stream_go_through_text.txt", 'w')
    for word in tqdm(text[1:], file=file_):
        if current_word not in nodes:
            path_edges.append(("NF", word))
            current_word = word
            continue
        if word not in nodes:
            path_edges.append((current_word, "NF"))
            continue
        if word in graph.neighbors(nodes.index(current_word)):
            path_edges.append((current_word, word))
            file_.write('in path_edges!!!')
        else:
            try:
                shortest_path = tuple(graph.get_shortest_paths(nodes.index(current_word),nodes.index(word),weights='weight')[0])
                path_edges.append(shortest_path)
            except:
                path_edges.append(f"No path {current_word} -- {word}")
        current_word = word
    file_.close()
    return path_edges

def return_Arrays_of_path_length_withNFAndLimit(human_file_path,bot_file_path,graph,dia,limit):
    bot_paths = []
    human_paths = []
    counter = 0
    names = []
    for v in graph.vs:
        names.append(v['_nx_name'])
    with open(human_file_path) as file_1, open(bot_file_path) as file_2: 
        human = file_1.readlines()
        bot = file_2.readlines()
        for text1, text2 in zip(human, bot):
            counter += 1
            text2 = ' '.join(text2.split()[:limit])
            text1 = ' '.join(text1.split()[:len(text2.split())])
            path_length_text_1 = 0
            path_length_text_2 = 0
            for path in go_through_text_with_NF(text1 , graph,names):
                if "NF" in path:
                    path_length_text_1+=dia
                else:
                    for index in range(1,len(path)):
                        path_length_text_1+= graph.es[graph.get_eid(path[index-1],path[index])]['weight']
            for path in go_through_text_with_NF(text2 , graph,names):
                if "NF" in path:
                    path_length_text_2+=dia
                else:
                    for index in range(1,len(path)):
                        path_length_text_1+= graph.es[graph.get_eid(path[index-1],path[index])]['weight']

            human_paths.append(path_length_text_1)
            bot_paths.append(path_length_text_2)
    return np.array(human_paths) , np.array(bot_paths)

def convert_text_shortest_paths_to_text_words_path_num2word(shortest_paths: list,names: list) -> list:
    '''
    Convert text shortest paths to text words path

    Parameters
    ----------
    shortest_paths: list

    Returns
    -------
    words_path : list

    shortest_paths = [(word_1, word_1_1, word_1_2, ..., word_1_n, word_2),
                      (word_2, ..., word_3),
                      (word_3, ..., word_4) ..., (word_n-1, ..., word_n)]
    words_path = [word_1, word_1_1, word_1_2, word_1_3,
                   ...,
                  word_n-1, word_n-1_1,
                   ...,
                  word_n-1_k, word_n]
    '''
    words_path = []
    try:
        for number in shortest_paths[0]:
            words_path.append(names[number])
        for short_path in shortest_paths[1:]:
            for number in short_path[1:]:
                words_path.append(names[number])
    except:
        words_path.append(0)
    return words_path

def calculate_average_centrality_for_path(path,centrality_dic):
    centrality_val = []
    #min_val = min(centrality_dic.values())
    for word in path:
        if word not in centrality_dic.keys():
            centrality_val.append(0.0)
        else:
            centrality_val.append(centrality_dic[word])
    #return np.average(centrality_val)
    return sum(centrality_val)

def return_Arrys_of_centralites(human_file_path , bot_file_path , graph,centrality_dic,limit):
    bot_average_centrality = []
    human_average_centrality = []
    names = []
    for v in graph.vs:
        names.append(v['_nx_name'])
    with open(human_file_path) as file_1, open(bot_file_path) as file_2: 
        human = file_1.readlines()
        bot = file_2.readlines()
        for text1, text2 in zip(human, bot):
            text2 = ' '.join(text2.split()[:limit])
            text1 = ' '.join(text1.split()[:len(text2.split())])
            cen_1 = calculate_average_centrality_for_path(convert_text_shortest_paths_to_text_words_path_num2word(go_through_text_without_NF(text1,graph,names),names),centrality_dic)
            cen_2 = calculate_average_centrality_for_path(convert_text_shortest_paths_to_text_words_path_num2word(go_through_text_without_NF(text2,graph,names),names),centrality_dic)
            human_average_centrality.append(cen_1/limit)
            bot_average_centrality.append(cen_2/limit)
    bot_average_centrality = np.array(bot_average_centrality)
    human_average_centrality = np.array(human_average_centrality)
    return human_average_centrality,bot_average_centrality

def go_through_text_without_NF(text: str, graph: ig.Graph, nodes: list) -> list:
    text = text.split()
    path_edges = []
    current_word = text[0]
    file_ = open("Ar_stream_go_through_text.txt", 'w')
    for word in tqdm(text[1:], file=file_):
        if current_word not in nodes:
            #path_edges.append(("NF", word))
            current_word = word
            continue
        if word not in nodes:
            #path_edges.append((current_word, "NF"))
            continue
        if word in graph.neighbors(nodes.index(current_word)):
            path_edges.append((nodes.index(current_word),nodes.index(word)))
            file_.write('in path_edges!!!')
        else:
            try:
                shortest_path = tuple(graph.get_shortest_paths(nodes.index(current_word),nodes.index(word),weights='weight')[0])
                path_edges.append(shortest_path)
            except:
                path_edges.append(f"No path {current_word} -- {word}")
        current_word = word
    file_.close()
    return path_edges
        
        
        

        
        

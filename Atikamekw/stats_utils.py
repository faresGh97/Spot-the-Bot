import networkx as nx
from tqdm import tqdm
import numpy as np

def go_through_text_with_NF(text: str, graph: nx.classes.graph.Graph) -> list:
    '''
    Convert text to path on NetworkX graph

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
    file_ = open("stream_go_through_text.txt", 'w')
    for word in tqdm(text[1:], file=file_):
        if current_word not in graph:
            path_edges.append(("NF", word))
            current_word = word
            continue
        if word not in graph:
            path_edges.append((current_word, "NF"))
            continue
        if word in graph[current_word]:
            path_edges.append((current_word, word))
            file_.write('in path_edges!!!')
        else:
            try:
                shortest_path = tuple(nx.dijkstra_path(graph, current_word, word))
                path_edges.append(shortest_path)
            except:
                path_edges.append(f"No path {current_word} -- {word}")
        current_word = word
    file_.close()
    return path_edges

def convert_text_shortest_paths_to_text_words_path_V2(shortest_paths: list) -> list:
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
        for word in shortest_paths[0]:
            words_path.append(word)
        for short_path in shortest_paths[1:]:
            for word in short_path[1:]:
                words_path.append(word)
    except:
        words_path.append(0)
    return words_path



def calculate_average_centrality_for_path(path,centrality_dic):
    centrality_val = []
    min_val = min(centrality_dic.values())
    for word in path:
        if word not in centrality_dic.keys():
            centrality_val.append(min_val)
        else:
            centrality_val.append(centrality_dic[word])
    return np.average(centrality_val)

def return_Arrys_of_centralites(human_file_path , bot_file_path , graph,centrality_dic):
    bot_average_centrality = []
    human_average_centrality = []
    #counter = 0
    with open(human_file_path) as file_1, open(bot_file_path) as file_2: 
        #counter += 1
        human = file_1.readlines()
        bot = file_2.readlines()
        for text1, text2 in zip(human, bot):
            cen_1 = calculate_average_centrality_for_path(convert_text_shortest_paths_to_text_words_path_V2(go_through_text_with_NF(text1 , graph)),centrality_dic)
            cen_2 = calculate_average_centrality_for_path(convert_text_shortest_paths_to_text_words_path_V2(go_through_text_with_NF(text2 , graph)),centrality_dic)
            human_average_centrality.append(cen_1)
            bot_average_centrality.append(cen_2)
    bot_average_centrality = np.array(bot_average_centrality)
    human_average_centrality = np.array(human_average_centrality)
        
    #X = np.arange(0,counter)
    return human_average_centrality,bot_average_centrality #,X


# def return_Arrays_of_path_length(human_file_path,bot_file_path,graph):
#     bot_paths = []
#     human_paths = []
#     counter = 0
#     with open(human_file_path) as file_1, open(bot_file_path) as file_2: 
#         human = file_1.readlines()
#         bot = file_2.readlines()
#         for text1, text2 in zip(human, bot):
#             counter += 1
#             text1 = text1[:len(text2)]
#             #print (text1[:len(text2)])
#             #print (text2)
#             path_length_text_1 = 0
#             path_length_text_2 = 0
#             for path in go_through_text(text1 , graph):
#                 path_length_text_1 += len(path)
#             for path in go_through_text(text2 , graph):
#                 path_length_text_2 += len(path)

#             human_paths.append(path_length_text_1)
#             bot_paths.append(path_length_text_2)
#     return np.array(human_paths) , np.array(bot_paths)


def return_Arrays_of_path_length_withNF(human_file_path,bot_file_path,graph,dia):
    bot_paths = []
    human_paths = []
    counter = 0
    with open(human_file_path) as file_1, open(bot_file_path) as file_2: 
        human = file_1.readlines()
        bot = file_2.readlines()
        for text1, text2 in zip(human, bot):
            counter += 1
            text1 = text1[:len(text2)]
            #print (text1[:len(text2)])
            #print (text2)
            path_length_text_1 = 0
            path_length_text_2 = 0
            for path in go_through_text_with_NF(text1 , graph):
                if "NF" in path:
                    path_length_text_1+=dia
                else:
                    path_length_text_1 += len(path)
            for path in go_through_text_with_NF(text2 , graph):
                if "NF" in path:
                    path_length_text_2+=dia
                else:
                    path_length_text_2 += len(path)

            human_paths.append(path_length_text_1)
            bot_paths.append(path_length_text_2)
    return np.array(human_paths) , np.array(bot_paths)
        

        
        
        

        
        

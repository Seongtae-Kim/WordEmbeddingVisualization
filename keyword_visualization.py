# Seongtae Kim 2020-06-14
# https://github.com/Seongtae-Kim/WordEmbeddingVisualization
from gensim.models import Word2Vec
def keyword_visualization(model, keyword, num_nodes=10, font_size=17):
    words = []
    vectors = []
    edges = []
    sizes = [ 5000 ] # center word size: 5000
    w2vs = internal_w2v.wv.most_similar(positive=[keyword], topn=num_nodes)
    
    i=1
    for w2v in w2vs:
        word = str(i) + "위\n" + w2v[0] + "\n"+ str(round(w2v[1], 3))
        words.append(word)
        vectors.append(w2v[1])
        edges.append((keyword, word))
        i += 1
    G = nx.Graph()
    G.add_node(keyword, weight=1)
    
    i=1
    for word, vector in zip(words, vectors):
        G.add_nodes_from(words, weight=vector)
        if int(i/10) in list(range(1, 10)):
            size = 5000 * round(vector, 2) #/ (i/30) <- if you remove this number sign the size of the nodes will be drastically smaller
        else: # The first ten sequence
            size = 5000 * round(vector, 2)
        sizes.append(size)
        i+=1
    G.add_edges_from(edges)
    
    labels_list = [keyword] + words
    labels = defaultdict()
    for label in labels_list:
        labels[label] = label
    labels = dict(labels)
        
    pos = nx.spring_layout(G) # edge layout (0, 1) -> (from, to)
    colors= range(num_nodes)
    #print(G.nodes(data="weight"))
    plt.figure(figsize=(16,12))
    plt.axis('off')
    nx.draw(G, pos, node_color="brown", node_size=sizes, width=4, with_labels=True, alpha=0.9,
           font_family='NanumGothic', font_size=font_size) # You need NanumBothic font in matplotlib fontlist
    plt.savefig(keyword + "_" + str(num_nodes) + "_" + str(model) + ".png", format="PNG")
    

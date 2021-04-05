import networkx as nx
from networkx.algorithms import bipartite

G = nx.Graph()

numbers = range(3)
G.add_nodes_from(numbers, bipartite='customers')

letters = ['a', 'b']
G.add_nodes_from(letters, bipartite='products')

print(G.nodes(data=True))
print(G.edges())

# Degree centrality = number of neighbors/ number of possible neighbors
cust_nodes = [n for n, d in G.nodes(data=True) if
                d['bipartite'] == 'customers']

print(cust_nodes)

print(nx.bipartite.degree_centrality(G, cust_nodes))
#loads undirected edgelist
#number of nodes
len(G)
#number of edges

"""measures of prominence"""
#Degree centrality 
degree_centrality(G)
#Degree centralization

#eigenvalue centrality.
eigenvector_centrality(G[, max_iter, tol, …])

#Closeness centrality
closeness_centrality
#Closeness centralization

#Betweenness centrality
betweenness_centrality
#Betweenness centralization

#Information centrality

"""measures of range"""
#reach
#diameter
diameter(G, e=None)
"""measures of cohesion"""
#density
density(G)
#reciprocity
reciprocity(G, nodes=None)
#clustering coefficient 
clustering(G[, nodes, weight])
#fragmentation

#asortivity

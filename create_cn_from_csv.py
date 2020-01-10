# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 23:57:43 2020

@author: icecream boi
"""
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('distances_between_all_flies.csv', index_col=0)

df = df.T

indexes = []
for i in range(len(df)):
    row = df.iloc[i]
    for value in row:
        if value <= 10:
            indexes.append(i)
                      
unique_list = [] 

for x in indexes:  
    if x not in unique_list: 
        unique_list.append(x) 
        
df = df.iloc[unique_list]

index_list = df.index.values.tolist()


G=nx.Graph()

how_much_nodes = 17
G.add_nodes_from([0,how_much_nodes])
number_of_nodes = len(G)

for element in index_list: 
    start, end = element.split(' ')
    G.add_edge(start, end)

nx.draw(G)
nx.draw_circular(G)

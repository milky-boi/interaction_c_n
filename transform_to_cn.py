"""
this part of script loads .csv tracking files of each flie. Every row are values taken from each frame by Flytrack software
"""

#load folder with .csv files, takes their x, y and velocity value
import os

path = '/home/firestarter/interaction_c_n/data'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
  
import pandas as pd 
import math 

distances = [] 
for i in range(len(df_1)):
    df_1 = pd.read_csv(files[11])
    df_2 = pd.read_csv(files[7])
    
    x1 = df_1.iloc[i]['pos x']
    y1 = df_1.iloc[i]['pos y']
    
    x2 = df_2.iloc[i]['pos x']
    y2 = df_2.iloc[i]['pos y']
    
    distance_df1_df2 = distance_between_points(x1, x2, y1, y2)
    distances.append(distance_df1_df2)

def distance_between_points(x1, x2, y1, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def matrix_of_distances():
    """crates matrix of distances between flies for each frame"""
    pass
    
for element in distances:
    if element <= 2:
        print(distances.index(element))

#function for touch criteria, if 2 flies spend time (15 frames, depends on fps ) near eachother (interacting), edge between 2 nodes of flies will be created
#matrix analysis, 15, consecutive frames must have True criteria  
#output is edge list between nodes in graph, each node is flie and their interaction is edge

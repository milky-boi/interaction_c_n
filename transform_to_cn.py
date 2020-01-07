"""
this part of script loads .csv tracking files of each flie. 
Every row are values taken from each frame by Flytrack software
"""
import os
import pandas as pd 
import math 
import time 

def distances_f(df1, df2):
    distances = []
    for i in range(len(df1)):
        x1 = df1.iloc[i]['pos x']
        y1 = df1.iloc[i]['pos y']        
        x2 = df2.iloc[i]['pos x']
        y2 = df2.iloc[i]['pos y']
        
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distances.append(dist)
        
    return distances

def distances_flies():
    start_time = time.time()
    
    path = r'H:\0_theory\interaction_c_n/data'
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))
      
    all_distances = []
    all_pairs = []
    
    for i in range(len(files)):
        df1 = pd.read_csv(files[i])   
        next_flie = i + 1
        
        if next_flie <= len(files):     
            for j in range(next_flie, len(files)):
                df2 = pd.read_csv(files[j])         
                #globals()['df' + str(i) + '_df' + str(j)] = distances_f(df1, df2)
                all_distances.append(distances_f(df1, df2))
                all_pairs.append(str(i) + ' ' + str(j))
                   
    df_distances = pd.DataFrame.from_records(all_distances)
    df_distances = df_distances.T
    df_distances.columns = all_pairs
    
    df_distances.to_csv('distances_between_flies.csv')
    
    clean_time = time.time()-start_time
    print("Distances calculated in %.2f" % clean_time + " seconds")
    print('distances between flies saved to .csv')



def main():
    distances_flies()
    
if __name__ == '__main__':
    main()


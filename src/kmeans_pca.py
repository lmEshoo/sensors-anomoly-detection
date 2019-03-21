import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

cols =  ['MagX', 'MagY', 'MagZ', 'AccX', 'AccY', 'AccZ', 'GyroR', 'GyroP', 'GyroY']
data = pd.read_csv("../data/formatted_online_sensor_data.csv") 

# subset = data
# tuples = [tuple(x) for x in subset.values]
# data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.6, random_state=50)
# Preview the first 5 lines of the loaded data 
# print(data.head())
# print(tuples)
# print(data.values[:,1])

clusters = 3
  
kmeans = KMeans(n_clusters = clusters) 
kmeans.fit(data) 
  
print(kmeans.labels_)
pca = PCA(9) 
pca.fit(data) 
  
pca_data = pd.DataFrame(pca.transform(data)) 

from matplotlib import colors as mcolors 
import math 
   
''' Generating different colors in ascending order  
                                of their hsv values '''
colors = list(zip(*sorted(( 
                    tuple(mcolors.rgb_to_hsv( 
                          mcolors.to_rgba(color)[:3])), name) 
                     for name, color in dict( 
                            mcolors.BASE_COLORS, **mcolors.CSS4_COLORS 
                                                      ).items())))[1] 
   
   
# number of steps to taken generate n(clusters) colors  
skips = math.floor(len(colors[5 : -5])/clusters) 
cluster_colors = colors[5 : -5 : skips] 
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
   
fig = plt.figure() 
ax = fig.add_subplot(111, projection = '3d') 
ax.scatter(pca_data[0], pca_data[1], pca_data[2],  
           c = list(map(lambda label : cluster_colors[label], 
                                            kmeans.labels_))) 
   
str_labels = list(map(lambda label:'% s' % label, kmeans.labels_)) 
   
list(map(lambda data1, data2, data3, str_label: 
        ax.text(data1, data2, data3, s = str_label, size = 16.5, 
        zorder = 20, color = 'k'), pca_data[0], pca_data[1], 
        pca_data[2], str_labels)) 
plt.savefig('../outputs/kmeans_pca_1.png')

from matplotlib import cm 
  
# generating correlation data 
df = data.corr() 
df.index = range(0, len(df)) 
df.rename(columns = dict(zip(df.columns, df.index)), inplace = True) 
df = df.astype(object) 
  
''' Generating coordinates with  
corresponding correlation values '''
for i in range(0, len(df)): 
    for j in range(0, len(df)): 
        if i != j: 
            df.iloc[i, j] = (i, j, df.iloc[i, j]) 
        else : 
            df.iloc[i, j] = (i, j, 0) 
  
df_list = [] 
  
# flattening dataframe values 
for sub_list in df.values: 
    df_list.extend(sub_list) 
  
# converting list of tuples into trivariate dataframe 
plot_df = pd.DataFrame(df_list) 
  
fig = plt.figure() 
ax = Axes3D(fig) 
  
# plotting 3D trisurface plot 
ax.plot_trisurf(plot_df[0], plot_df[1], plot_df[2],  
                    cmap = cm.jet, linewidth = 0.2)
plt.savefig('../outputs/kmeans_pca_2.png')
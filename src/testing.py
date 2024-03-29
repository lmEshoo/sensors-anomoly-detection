# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm
from datetime import datetime
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import GroupKFold

# X = np.array([18,18,17,18,20,23,26,31,38,47,50,52,55,58,62,64,66,68,71,74,75,76,78,79,80,83,85,86,88,90,91,92,95,95,95,97,99,101,102,104,104,104,104,104,98,96,95,92,91,90,89,85,81,77,71,69,68,66,66,61,60,58,54,48,44,40,36,32,29,27,27,24,22,20,18,16,15,14,14,12,11,11,13,12,9,8,8,8,7,8,8,8,7,6,8,8,6,7,7,6])
# le = preprocessing.LabelEncoder()
# le.fit(X)
# print(le.classes_)
# print(lb.transform(X))
# print(lb.fit_transform(X)[0])

# X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# y = np.array([1, 2, 3, 4])
# groups = np.array([0, 1, 2])
# group_kfold = GroupKFold(n_splits=100)
# group_kfold.get_n_splits(X)
# print(group_kfold)
# # GroupKFold(n_splits=2)
# for train_index, test_index in group_kfold.split(X,groups=groups):
#     print("TRAIN:", train_index, "TEST:", test_index)
#     X_train, X_test = X[train_index], X[test_index]
#     # y_train, y_test = y[train_index], y[test_index]
#     print(X_train, X_test)
################
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# %matplotlib inline

# df = pd.DataFrame({
#     'x': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
#     'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
# })

# df = pd.DataFrame({
#     'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
#     'y': [18,18,17,18,20,23,26,31,38,47,50,52,55,58,62,64,66,68,71,74,75,76,78,79,80,83,85,86,88,90,91,92,95,95,95,97,99,101,102,104,104,104,104,104,98,96,95,92,91,90,89,85,81,77,71,69,68,66,66,61,60,58,54,48,44,40,36,32,29,27,27,24,22,20,18,16,15,14,14,12,11,11,13,12,9,8,8,8,7,8,8,8,7,6,8,8,6,7,7,6]
# })

# print(len(df['x']))
# print(len(df['y']))
# print(len(X))
# np.random.seed(200)
# k = 3
# # centroids[i] = [x, y]
# centroids = {
#     i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
#     for i in range(k)
# }
    
# fig = plt.figure(figsize=(10, 10))
# plt.scatter(df['x'], df['y'], color='k')
# colmap = {1: 'r', 2: 'g', 3: 'b'}
# for i in centroids.keys():
#     plt.scatter(*centroids[i], color=colmap[i])
# plt.xlim(0, 120)
# plt.ylim(0, 120)
# plt.savefig(str(datetime.now())+'.png')
############
# from sklearn.cluster import KMeans
# import numpy as np
# x = np.random.random(13876)

# km = KMeans()
# print(km.fit(x.reshape(-1,1)))

############
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
cols =  ['MagX', 'MagY', 'MagZ', 'AccX', 'AccY', 'AccZ', 'GyroR', 'GyroP', 'GyroY']
data = pd.read_csv("../data/formatted_online_sensor_data.csv") 

from sklearn.decomposition import PCA

pca = PCA(n_components=3)
pca_result = pca.fit_transform(df[feat_cols].values)

df['pca-one'] = pca_result[:,0]
df['pca-two'] = pca_result[:,1] 
df['pca-three'] = pca_result[:,2]

print ('Explained variation per principal component:', pca.explained_variance_ratio_)

from ggplot import *

chart = ggplot( df.loc[rndperm[:3000],:], aes(x='pca-one', y='pca-two', color='label') ) \
        + geom_point(size=75,alpha=0.8) \
        + ggtitle("First and Second Principal Components colored by digit")
chart
# subset = data
# tuples = [tuple(x) for x in subset.values]
# data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.6, random_state=50)
# Preview the first 5 lines of the loaded data 
# print(data.head())
# print(tuples)
# print(data.values[:,1])

# clusters = 3
  
# kmeans = KMeans(n_clusters = clusters) 
# kmeans.fit(data) 
  
# print(kmeans.labels_)
# pca = PCA(9) 
# pca.fit(data) 
  
# pca_data = pd.DataFrame(pca.transform(data)) 

# from matplotlib import colors as mcolors 
# import math 
   
# ''' Generating different colors in ascending order  
#                                 of their hsv values '''
# colors = list(zip(*sorted(( 
#                     tuple(mcolors.rgb_to_hsv( 
#                           mcolors.to_rgba(color)[:3])), name) 
#                      for name, color in dict( 
#                             mcolors.BASE_COLORS, **mcolors.CSS4_COLORS 
#                                                       ).items())))[1] 
   
   
# # number of steps to taken generate n(clusters) colors  
# skips = math.floor(len(colors[5 : -5])/clusters) 
# cluster_colors = colors[5 : -5 : skips] 
# from mpl_toolkits.mplot3d import Axes3D 
# import matplotlib.pyplot as plt 
   
# fig = plt.figure() 
# ax = fig.add_subplot(111, projection = '3d') 
# ax.scatter(pca_data[0], pca_data[1], pca_data[2],  
#            c = list(map(lambda label : cluster_colors[label], 
#                                             kmeans.labels_))) 
   
# str_labels = list(map(lambda label:'% s' % label, kmeans.labels_)) 
   
# list(map(lambda data1, data2, data3, str_label: 
#         ax.text(data1, data2, data3, s = str_label, size = 16.5, 
#         zorder = 20, color = 'k'), pca_data[0], pca_data[1], 
#         pca_data[2], str_labels)) 
# plt.savefig(str(datetime.now())+'.png')

# from matplotlib import cm 
  
# # generating correlation data 
# df = data.corr() 
# df.index = range(0, len(df)) 
# df.rename(columns = dict(zip(df.columns, df.index)), inplace = True) 
# df = df.astype(object) 
  
# ''' Generating coordinates with  
# corresponding correlation values '''
# for i in range(0, len(df)): 
#     for j in range(0, len(df)): 
#         if i != j: 
#             df.iloc[i, j] = (i, j, df.iloc[i, j]) 
#         else : 
#             df.iloc[i, j] = (i, j, 0) 
  
# df_list = [] 
  
# # flattening dataframe values 
# for sub_list in df.values: 
#     df_list.extend(sub_list) 
  
# # converting list of tuples into trivariate dataframe 
# plot_df = pd.DataFrame(df_list) 
  
# fig = plt.figure() 
# ax = Axes3D(fig) 
  
# # plotting 3D trisurface plot 
# ax.plot_trisurf(plot_df[0], plot_df[1], plot_df[2],  
#                     cmap = cm.jet, linewidth = 0.2)
# plt.savefig(str(datetime.now())+'.png')
# X = np.array([18.06875467, 18.12599897, 17.56173372, 18.36315393, 18.87017488, 20.0723052, 23.85042906, 26.90891027, 31.47618771, 38.58265877, 47.82761335, 50.84111691, 52.76697874, 55.00359535, 58.39327574, 62.13868856, 64.90277052, 66.51787758, 68.6195612, 71.57990932, 74.24994707, 75.50114393, 76.9608736, 78.03215981, 79.65544462, 80.87801933, 83.22503567, 85.3430748, 86.61062717, 88.90448809, 90.36830664, 91.65630341, 92.63763428, 95.09913921, 95.15638351, 95.88420391, 97.77735472, 99.92810488, 101.6495228, 102.9252529, 104.1273832, 104.8920035, 104.5485377, 104.6875596, 104.2541385, 98.82410765, 96.06411457, 95.28313875, 92.55176783, 91.29239321, 90.38875103, 89.66093063, 85.37987471, 81.8021059, 77.53740549, 71.96835279, 69.78898048, 68.07982922, 66.86134338, 66.21938944, 61.66028976, 60.50722599, 58.46687555, 54.71328497, 48.99703264, 44.54424381, 40.42674303, 36.21110916, 32.3184967, 29.37859297, 27.13788748, 27.47317553, 24.30838346, 22.02270031, 20.16226053, 18.2159543, 16.28600359, 15.09205103, 14.02485371, 14.02485371, 12.45881319, 11.1749053, 11.95179224, 13.19481134, 12.21348047, 9.154999256, 8.230912685, 8.729755878, 8.120512962, 7.302737236, 8.288156986, 8.881044388, 8.079624176, 7.875180244, 6.787538528, 8.091890812, 8.006024361, 6.914293766, 7.482647896, 7.004249096, 6.869316101, 6.047451496, 6.194651127, 5.605852604, 6.914293766, 7.335448265, 10.5247736, 16.98111296, 24.627316, 30.20454645, 35.78995466, 39.60078955, 44.41748857, 47.94210196, 49.82298613, 53.4825325, 55.96857071, 59.09656286, 61.22686863, 64.25263882, 67.40516424, 70.99519968, 74.58523512, 76.37616396, 79.4878006, 81.36050701, 82.42770433, 83.6584568, 82.23552704, 85.51071882, 93.68029833, 100.4024148, 103.1869411, 107.1286201, 107.5579524, 107.7215075, 105.6566238, 111.2870097, 95.79833746, 83.98556709, 71.73937559, 28.45041752, 49.23009872, 40.47989845, 26.73717737, 15.71356058, 29.86108065, 46.41286135, 59.48909521, 64.75557089, 132.1852684, 128.5298109, 123.5904455, 120.8754301, 118.8064575, 116.1037087, 97.51157761, 79.50824499, 72.90879488, 66.07218981, 64.67379332, 61.45584583, 53.91595364, 45.91810703, 38.44772577, 31.09183311, 27.10926533, 23.43336344, 21.06590271, 19.82697248, 24.45149422, 31.00596666, 39.75616693, 50.12965202, 60.36820412, 69.11431551, 76.5601635, 84.75836515, 91.55817032, 99.13077354, 103.0438304, 108.1058621, 105.3295135, 263.1356955, 137.6643658, 113.2455826, 101.2201905, 96.17860317, 84.00601149, 66.90223217, 50.17054081, 34.63280201, 25.24473667, 15.69311619, 13.29703331, 13.47285509, 16.07747078, 22.19852209, 23.06536436, 23.74002934, 26.47548914, 34.35884714, 46.83401585, 59.61176157, 71.59626484, 80.05615473, 88.1357789, 96.75104618, 104.3072939, 112.0802522, 117.9845929, 122.0652938, 120.4256535, 117.9396152, 121.6236949, 129.9936295, 128.8119435, 122.4987149, 143.9367056, 116.5780187, 121.0021853, 120.2252984, 134.6304178, 116.9582844, 116.9419289, 114.2187357, 111.5364313, 108.7805271, 108.2285285, 104.7284484, 102.4591208, 98.80775213, 90.49506187, 82.81205893, 76.74007416, 70.0343132, 61.2514019, 53.4252882, 46.82992697, 40.19776583, 33.99902582, 28.81023884, 23.68687391, 19.07052994, 11.88637018, 14.15569782, 27.24010944, 43.38300228, 57.68589973, 69.81760263, 80.6163311, 90.29470682, 100.4841924, 137.9096985, 115.7520652, 3328.011918, 4.849410057, 106.9773316, 116.3572192, 104.3195605, 108.7437272, 105.6811571, 94.64527369, 75.65652132, 55.40021658, 38.844347, 28.94108295, 27.08882093, 31.76649809, 60.7157588, 57.44056702, 51.0332942, 260.9358788, 41.53891802, 56.34883642, 85.94005108, 22.36616611, 290.6006932, 74.00870323, 28.72846127, 3349.085999, 4.77989912, 51.69569254, 36.67315245, 262.1870756, 55.00359535, 25.51869154, 22.51745462, 28.39317322, 68.7912941, 99.42926168, 101.4982343, 70.57404518, 26.88028812, 75.78327656, 48.71081114, 29.74659204, 180.9410572, 61.22277975, 21.58927917, 77.69687176, 68.57049465, 23.84634018, 56.43470287, 85.94413996, 80.35873175, 37.78123856, 24.95851517, 69.42098141, 290.1590943, 34.95173454, 34.80862379, 295.1679707, 239.3588662, 93.09558868, 38.50497007, 26.9988656, 83.52352381, 212.2332454, 43.08860302, 35.58959961, 299.1546273, 43.57926846, 41.93553925, 111.2297654, 56.91719055, 25.21202564, 37.06159592, 32.84596205, 28.05379629, 29.59939241, 31.99956417, 30.58072329, 206.4924598, 112.2233629, 63.39806318, 34.28524733, 296.5336561, 88.68777752, 49.60218668, 27.55904198, 64.94774818, 81.75712824, 39.82567787, 28.90428305, 70.6844449, 89.48510885, 44.34388876, 20.00688314, 61.98331118, 81.97792768, 252.9789209, 103.4118295, 103.3627629, 107.7542186, 291.2712693, 99.01628494, 127.98599, 93.22234392, 75.82416534, 33.87635946, 13.67321014, 37.47866154, 42.04185009, 106.1350226, 98.23122025, 54.61515188, 11.8822813, 9.29402113, 7.813847065, 16.33915901, 44.52379942, 73.58345985, 92.00794697, 109.7209692, 113.9979362, 115.2900219, 131.9522023, 127.2622585, 101.3796568, 67.38471985, 23.31887484, 7.760691643, 9.968686104, 11.57561541, 17.88884401, 30.58072329, 54.89319563, 79.78628874, 102.2219658, 110.4119897, 107.9545736, 107.975018, 88.36475611, 62.58028746, 36.0311985, 20.81239223, 11.4611268, 7.323181629, 3.545057774, 3.455102444, 3.271102905, 2.796792984, 2.98897028, 3.01759243, 3.160703182, 4.248344898, 9.428954124, 30.18410206, 51.41764879, 67.05352068, 79.945755, 87.78004646, 90.88350534, 91.92208052, 91.94661379, 90.84670544, 91.71763659, 92.68261194, 95.15638351, 102.5736094, 110.4733229, 115.6171322, 122.6132035, 117.3957944, 133.8617086, 116.5085077, 124.7762203, 115.6375766, 121.4724064, 118.5365915, 116.5616632, 134.2951298, 113.601315, 115.658021, 116.7129517, 109.8313689, 106.5030217, 95.03371716, 76.12674236, 52.24769115, 38.05110455, 27.05202103, 17.37773418, 14.04120922, 10.9254837, 11.52654886, 19.45079565, 33.65556002, 42.43847132, 52.32537985, 63.14864159, 69.09796, 71.24462128, 73.48532677, 74.46256876, 75.14950037, 76.92816257, 104.1314721, 112.5627398])
# Y = np.array([])
# print(np.percentile(data, [25,50,75]))
# print(len(data.values[0]))
# create kmeans object
# scatter_matrix(data, alpha=0.2, figsize=(6, 6), diagonal='kde')
# plt.savefig(str(datetime.now())+'.png')

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))

# x = data.values[:,0]
# y = data.values[:,1]

# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z');
# plt.savefig(str(datetime.now())+'.png')
# points = data.values[0]
# kmeans = KMeans(n_clusters=4)
# # fit kmeans object to data
# kmeans.fit(points)
# # print location of clusters learned by kmeans object
# print(kmeans.cluster_centers_)
# # save new clusters for chart
# y_km = kmeans.fit_predict(points)
# nd=pd.qcut(X,3, labels=[0,1,2])
# nd2=pd.qcut(data,3, labels=["close","not close","far"])

# for i in range(len(data)):
#     print(data[i],nd2[i])
# #     Y = np.append(Y,nd[i])

# # print(len(X),len(Y))
# # print(X[0],Y[0],nd2[0])
# #Plots
# trace = go.Scatter(
#     x = X,
#     y = nd2,
#     mode = 'markers'
# )
# # print(Y.reshape(Y.shape[0], -1),X.shape[0])
# data = [trace]
# py.plot(data, filename='blah.html')

# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score
# def p(clf, test_x):
#     pred = clf.predict([[test_x]])
#     if(pred[0] == 0):
#         pred = "close"
#     elif(pred[0] == 1):
#         pred = "not close"
#     else:
#         pred = "far"
#     conf = clf.decision_function([[test_x]])
#     print("test:",test_x,"\npredict:", pred,"\nconfidence out of 3 classes:", conf)

# clf = SVC(kernel='linear')
# clf.fit(X.reshape(X.shape[0], -1), Y.reshape(Y.shape[0]))
# p(clf,4005)
# p(clf,45)
# p(clf,5)


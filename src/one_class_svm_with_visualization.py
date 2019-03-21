import numpy as np
from sklearn import svm

import pandas as pd
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# choose file to use
filename = "formatted online sensor data.csv"
# filename = "formatted rdu-weather-history.csv"
# filename = "formatted training_data.csv"
# filename = "formatted training_data_new.csv"

# parse input csv
input_data = np.array(pd.read_csv(filename))
total_elements = np.size(input_data,0)  # number of records in file
training_sample_size = int(round(total_elements*7/10))  # desired training sample size (currently 70% in train, 30% in test)
print("Total elements loaded: %i" % total_elements)
print("Training size: %i" % training_sample_size)

# assign input data to train and test randomly (70% in train, 30% in test)
randomized_data = input_data[np.random.permutation(input_data.shape[0])]
X_train = randomized_data[0:training_sample_size]
X_test = np.sort(randomized_data[training_sample_size:total_elements+1],axis=0)

# fit the model - nu is set to output approximately 5% anomalous data
clf = svm.OneClassSVM(nu=0.05, kernel="rbf", gamma=.00005)
# clf = svm.OneClassSVM(nu=0.1, kernel="linear")
clf.fit(X_train)

# assign prediction labels
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size

# print tensors and assigned labels for testing data
for i in range(total_elements-training_sample_size-1):
    print("Test data:", end =" ")
    print(X_test[i], end =" ")
    print("Label: %i" % (y_pred_test[i]))

# print anomalous counts
print("training anomalies: %i / %i" % (n_error_train, training_sample_size))
print("test anomalies: %i / %i" % (n_error_test, total_elements - training_sample_size))

# visualization of high dimensional data to 2D and 3D
feat_cols = ['pixel'+str(i) for i in range(X_test.shape[1])]

df = pd.DataFrame(X_test,columns=feat_cols)
df['label'] = y_pred_test

pca = PCA(n_components=3)
pca_result = pca.fit_transform(df[feat_cols].values)

df['pca-one'] = pca_result[:,0]
df['pca-two'] = pca_result[:,1]
df['pca-three'] = pca_result[:,2]

print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

# 2D
twodee = plt.scatter(df['pca-one'], df['pca-two'], c=df['label'])

# 3D
threedee = plt.figure().gca(projection='3d')
threedee.scatter(df['pca-one'], df['pca-two'], df['pca-three'], c=df['label'])
threedee.set_xlabel('pca-one')
threedee.set_ylabel('pca-two')
threedee.set_zlabel('pca-three')
plt.show()

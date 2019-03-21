import numpy as np
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

data = pd.read_csv("../data/training_data.csv")
# print(data.head())
X = data.values[:,0]
Y = np.array([])
np.percentile(X, [25,50,75])

nd=pd.qcut(X,3, labels=[0,1,2])
nd2=pd.qcut(X,3, labels=["close","not close","far"])

for i in range(len(X)):
    # print(X[i],nd2[i])
    Y = np.append(Y,nd[i])

# print(len(X),len(Y))
# print(X[0],Y[0],nd2[0])
#Plots
trace = go.Scatter(
    x = X,
    y = nd2,
    mode = 'markers'
)
# print(Y.reshape(Y.shape[0], -1),X.shape[0])
data = [trace]
py.plot(data, filename='../outputs/cluster_percentile.html')

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
def p(clf, test_x):
    pred = clf.predict([[test_x]])
    if(pred[0] == 0):
        pred = "Anomalous"
    elif(pred[0] == 1):
        pred = "not close"
    else:
        pred = "far"
    conf = clf.decision_function([[test_x]])
    print("test:",test_x,"\npredict:", pred,"\nconfidence out of 3 classes:", conf)

clf = SVC(kernel='linear')
clf.fit(X.reshape(X.shape[0], -1), Y.reshape(Y.shape[0]))
p(clf,405)
p(clf,55)
p(clf,155)
p(clf,5)
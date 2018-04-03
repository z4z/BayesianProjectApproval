import pickle
import numpy as np

features = pickle.load(open("features","rb"))
dates = pickle.load(open("dates","rb"))
features = np.hstack((dates,features))
length = dates.max()+1
avg_features = np.zeros((length,features.shape[1]))
for i in range(0,length):
    indices = np.nonzero(dates[:,0]==i)
    avg_features[i,:]=(sum(features[indices],0)/len(indices[0]))


                       
pickle.dump(avg_features,open("avg_features","wb"))


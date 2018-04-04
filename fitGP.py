import pickle
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, Matern, WhiteKernel
import matplotlib.pyplot as plt


features = pickle.load(open("avg_features","rb"))
Y = pickle.load(open("approval","rb"))

#normalize day
features[:,0]=features[:,0]/433

kernel = Matern(nu=0.5)+WhiteKernel()
gp = GaussianProcessRegressor(kernel=kernel,normalize_y=True).fit(features[:350],Y[:350])
m,s = gp.predict(features,return_std=True)
plt.figure()
plt.plot(Y)
plt.plot(m)
plt.axvline(x=350,linestyle='--',color='red')
plt.title("GP with Matern kernel nu=0.5")
plt.xlabel("Days since Inauguration")
plt.ylabel("Approval Rating")
plt.savefig("Matern_10feat.png")
plt.show()
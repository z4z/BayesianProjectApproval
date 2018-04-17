import csv
from matplotlib import pyplot as plt
import numpy as np
import pickle

data = []
csvfile = open('generic_topline.csv')
for row in reversed(list(csv.reader(csvfile))):
    data.append(row)
del(data[-1])

dem_estimates = []
rep_estimates = []
for row in data:
	subgroup = row[0]
	date = row[1]
	dem = float(row[2])
	rep = float(row[5])

	if subgroup == 'All polls':
		dem_estimates.append(dem)
		rep_estimates.append(rep)

dem_array = np.array(dem_estimates)
rep_array = np.array(rep_estimates)

pickle.dump(dem_array, open("dem_estimates", "wb"))
pickle.dump(rep_array, open("rep_estimates", "wb"))

plt.plot(dem_estimates)
plt.plot(rep_estimates)
plt.show()
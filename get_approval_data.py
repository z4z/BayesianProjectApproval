import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import pickle

plt.close("all")

# https://projects.fivethirtyeight.com/trump-approval-ratings/historical-approval.json
other_approval_json = json.load(open('historical-approval.json'))

# https://projects.fivethirtyeight.com/trump-approval-ratings/approval.json
trump_approval_json = json.load(open('trump-approval.json'))

#pprint(other_approval_json)

presidents = {}
for data in other_approval_json:
	president = data['president']
	if president not in presidents:
		presidents[president] = []
	president_approval = presidents[president]
	approval = data['approve_estimate']
	president_approval.append(approval)

trump_approval = []
approval_var = []
approval_std = []
date_today = '2018-04-02'
for data in trump_approval_json:
	if (data['date'] == date_today): break
	if (data['subgroup'] == 'All polls'): # 'Adults' 'Voters'
		approval = float(data['approve_estimate'])
		trump_approval.append(approval)
		high = float(data['approve_hi'])
		low = float(data['approve_lo'])
		dev = high-approval
		num_stds = 1.64 # 90% confidence interval
		std = dev / num_stds
		approval_std.append(std)
		var = std * std
		approval_var.append(var)
print(approval_var)
print(np.mean(approval_var))
print(np.mean(approval_std) ** 2)

pickle.dump(approval_var, open("approval_vars", "wb"))

presidents['Donald Trump'] = trump_approval

trump_array = np.array(trump_approval)
pickle.dump(trump_array, open("approval","wb"))

rep_approval = pickle.load(open("rep_estimates","rb"))

plt.plot(trump_approval[82:])
plt.plot(rep_approval[:-15])
plt.show()


# for president, approval in presidents.items():
# 	plt.figure()
# 	plt.plot(approval)
# 	plt.title(president)

#plt.show()


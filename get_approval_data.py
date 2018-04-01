import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

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
date_today = '2018-03-29'
for data in trump_approval_json:
	if (data['date'] == date_today): break
	if (data['subgroup'] == 'All polls'): # 'Adults' 'Voters'
		trump_approval.append(data['approve_estimate'])
presidents['Donald Trump'] = trump_approval


for president, approval in presidents.items():
	plt.figure()
	plt.plot(approval)
	plt.title(president)

plt.show()


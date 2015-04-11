import os
os.chdir("C:\Users\eng d\Documents\GitHub\Twitter-Sentiment-Analysis\Data")

from pandas.io.parsers import read_csv
import numpy as np

tweets = read_csv("working_data.csv")
threshold = tweets["candidate"]
time = tweets["minutes"]


other = []
proobama = []
promccain = []
mixed = []

#prints time of every instance, e.g. where candidate = 1 (proobama). THIS PART WORKS FOR SURE
def times_list(key):
    time_instance = []
    for ind, row in enumerate(threshold):
        if row == key:
            time_instance.append(time[ind])
    return time_instance
combined = times_list(1) + times_list(2)

# counts the number of instances for times (in minutes) from 1 to 150, where candidate = 1 (proobama)
def full_freq_list(polit_opinion):
    freq_counter = []
    for minute in range(0,151):
        if (minute in times_list(polit_opinion)) == True:
            freq_counter.append(times_list(polit_opinion).count(minute))
        else:
            freq_counter.append(0)
    return freq_counter

proobama = full_freq_list(1)
promccain = full_freq_list(2)
mixed = full_freq_list(3)
other = full_freq_list(0)

#makes a 100% stack plot

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches


republican = mpatches.Patch(color='green', label='Republican')
democrat = mpatches.Patch(color='blue', label='Democrat')



y = np.row_stack((proobama,promccain))
x = range(0,151)

# Make new array consisting of fractions of column-totals,
# using .astype(float) to avoid integer division
percent = y /  y.sum(axis=0).astype(float) * 100 

fig = plt.figure()
ax = fig.add_subplot(111)

ax.stackplot(x, percent)
ax.set_title('Opinions in tweets over time')
ax.set_ylabel('Percent (%)')
ax.margins(0, 0) # Set margins to avoid "whitespace"

plt.legend(handles=[republican,democrat],bbox_to_anchor=(1.12, 1.05))

# plt.show()
savefig('obamamccainstackplot.pdf')
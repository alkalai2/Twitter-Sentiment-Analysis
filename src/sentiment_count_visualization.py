# -*- coding: utf-8 -*-
#counts number of instances of every type of value from column "x", given condition "threshold"

import os
os.chdir("C:\Users\eng d\Documents\GitHub\Twitter-Sentiment-Analysis\Data")

from pandas.io.parsers import read_csv
import numpy as np

tweets = read_csv("working_data.csv")
threshold = tweets["candidate"]
value2 = tweets["minutes"]

#counts unique values
def unique_list(mins):
    uniq_keys = np.unique(mins)
    return uniq_keys

def count_unique(keys):
    uniq_keys = np.unique(keys)
    bins = uniq_keys.searchsorted(keys)
    return np.bincount(bins)

# def count_unique(keys):
#     uniq_keys = np.unique(keys)
#     bins = uniq_keys.searchsorted(keys)
#     return uniq_keys, np.bincount(bins) #bincount zlicza częstotliwości, a uniq_keys zawiera wartości częstotliwości


#makes a list of indices to be retrieved from the "minutes" column
def index_list(condition):
    list_of_indices = []
    for ind, row in enumerate(threshold):
        if row == condition:
            list_of_indices.append(ind)
    return list_of_indices

proobama = value2[index_list(1)]
other = value2[index_list(0)]
promccain = value2[index_list(2)]
mixed = value2[index_list(3)]
# print unique_list(x)
# print count_unique(x)

import matplotlib.pyplot as plt
plt.plot(unique_list(proobama),count_unique(proobama),label="Democrat")
# plt.plot(unique_list(other), count_unique(other),label="Other")
# plt.plot(unique_list(promccain),count_unique(promccain),label="Republican")
plt.plot(unique_list(mixed),count_unique(mixed),label="Mixed")

plt.xlabel("minutes into the debate")
plt.ylabel("opinion count")
plt.title("counts of types of statements over time")
plt.legend()

plt.show()
# savefig('testgraph.png')
import statistics
import math
import random

import pandas
import matplotlib.pyplot as plt


fifa19_df = pandas.read_csv('C:/Users/guru.08/Desktop/Materials/Original modules/Dataset/data.csv')

pop = fifa19_df['Jersey Number']

pop_as_list = [i for i in pop if not math.isnan(i)]

n = len(pop_as_list)
print(n)

fig,ax = plt.subplots()

h = ax.hist(pop_as_list)

#Experiment: Fifa wants to give a prize to a random player listed in the data.

#Prob distribution (X = winner's number of jersey)
nums = [1 + i for i in range(99)]
prob = [pop_as_list.count(i)/n for i in nums]

ax.plot(nums, prob, 'o')
fig.show()

#Prob distribution (X = winner's number of jersey between [1,11], [12, 22], [23, 33], [34, 44], \
#                                                         [45, 55], [56, 66], [67, 77], [78, 88], [89, 99])
h2 = ax.hist(pop_as_list, density = True, bins = 9, color = "blue")
fig.show()

#check law of large numbers
samples = [random.sample(pop_as_list, 1)[0] for i in range(200)]
ax.hist(samples, density = True, bins = 9, color = (1,0,0,0.2))
fig.show()

import statistics
import math
import random

import pandas
import matplotlib.pyplot as plt

source = "https://www.kaggle.com/karangadiya/fifa19"

fifa19_df = pandas.read_csv('C:/Users/guru.08/Desktop/Materials/Original modules/Dataset/data.csv')

population = fifa19_df['Jersey Number']

population_as_list = [i for i in population if not math.isnan(i)]

n = len(population_as_list)
print(n)

fig,ax = plt.subplots()

h = ax.hist(population_as_list)
#fig.show()


#Central Limit Theorem Simulation on the distribution for the sampling mean:

pop_mean = sum(population_as_list)/n
pop_sigma = statistics.stdev(population_as_list)

m = 500
samples = []
for i in range(7000):
    sample_mean = sum(random.sample(population_as_list,  m))/m
    samples.append(math.sqrt(m)*(sample_mean - pop_mean)/pop_sigma)

fig, ax = plt.subplots()

ax.hist(samples, bins = 30, density = True, color = "black")

standard_normal = [random.normalvariate(0, 1) for i in range(10000)] 

ax.hist(standard_normal, bins = 30, color = (1, 0, 0, 0.2), density = True)

fig.show()


#bootstrap (EXERCISE)

small_samples = random.sample(population_as_list, 10)



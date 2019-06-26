import random

#Roll a 6 sided dice:

#
sample = random.randint(1, 6)

#
for i in range(10):
    print(random.randint(1,6))

#
samples = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
print(samples)
samples.append(random.randint(1,6))
print(samples)

samples[0]
samples[1]
samples[2]
samples[3]

samples.append(999)
print(samples)

samples[-1] = random.randint(1,6)
print(samples)

#
samples = []
sixes = []
ones = []
for i in range(1000):
    sample = random.randint(1, 6)
    samples.append(sample)
    if sample == 6:
        sixes.append(sample)
    elif samples == 1:
        ones.append(sample)


# Roll two 6 sided dices:

#
samples = []
tens = []
threes = []
for i in range(10000):
    sample_dice_1 = random.randint(1, 6)
    sample_dice_2 = random.randint(1, 6)
    total = sample_dice_1 + sample_dice_2
    samples.append( total )
    if total == 10:
        tens.append(total)
    elif total == 3:
        threes.append(total)

# Visualization
import matplotlib.pyplot as plt

samples = []
for i in range(10000):
    sample_dice_1 = random.randint(1, 6)
    sample_dice_2 = random.randint(1, 6)
    total = sample_dice_1 + sample_dice_2
    samples.append( total )


totals = [samples.count(i+1)/len(samples) for i in range(12)]

fig, ax = plt.subplots()

x = [1,2,3,4,5,6,7,8,9,10,11,12]
ax.plot(x, totals, 'o')
fig.show()

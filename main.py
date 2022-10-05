

#b = ["saw", "small", "He", "foxes", "six"]
#b.sort(key=len)
#print(b)

import matplotlib.pyplot as plt
import random
position = 0
walk = [position]
nsteps = 1000
for _ in range(nsteps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
    plt.plot(walk[:100])








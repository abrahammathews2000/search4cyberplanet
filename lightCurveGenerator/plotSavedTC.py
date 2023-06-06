import numpy as np
import matplotlib.pyplot as plt

tc = np.loadtxt('./generatedData/Type00lc.csv', delimiter=',')
phase = np.loadtxt('./generatedData/phase.csv', delimiter=',')
#print(tc)
plt.scatter(phase,tc)
plt.show()
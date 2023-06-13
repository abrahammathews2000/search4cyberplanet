import numpy as np
import matplotlib.pyplot as plt

tc = np.loadtxt('./generatedData/lc/1_0lc.csv', delimiter=',')
phase = np.loadtxt('./generatedData/phase.csv', delimiter=',')
print("LEngth of TC = ",len(tc))
#print(tc)
plt.scatter(phase,tc)
plt.show()
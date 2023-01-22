import numpy as np
import matplotlib.pyplot as plt

x,y=np.loadtxt("test21.txt",unpack=True)
plt.plot(x,y)
plt.show()

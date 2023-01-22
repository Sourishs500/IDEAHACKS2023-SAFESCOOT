import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt
import Player
import temp
import firebase_unoptimizedpath


badroutefile = open(r"write.txt", "r")

# Generate random experimental data
#x = np.random.random(100)
#y = np.random.random(100)

x1 = []
y1 = []

text = badroutefile.read()
lns = text.splitlines()

for l in lns:
    x1.append(float(l.split(' ')[0]))
    y1.append(float(l.split(' ')[1]))

#x = list(map(float, x1))
#y = list(map(float, y1))

user_data = np.zeros((len(x1), 2))
user_data[:, 0] = x1
user_data[:, 1] = y1

"""
# Generate random numerical data
datapoints = 3
x = np.random.random(datapoints) 
y = np.random.random(datapoints) 
"""

x = []
y = []

# For the x array and y array, you can read from a file or directly load from the temp.f_lat and temp.f_lon variables
goodroutefile = open(r"userroutedata.txt", "r")
x1 = []
y1 = []
text = goodroutefile.read()
lns = text.splitlines()

for l in lns:
    x1.append(float(l.split(' ')[0]))
    y1.append(float(l.split(' ')[1]))


#x = temp.f_lat
#y = temp.f_lon

optimal_data = np.zeros((len(x1), 2))

optimal_data[:, 0] = x1
optimal_data[:, 1] = y1

# quantify the difference between the two curves using
# Discrete Frechet distance
df = 100 - similaritymeasures.frechet_dist(user_data, optimal_data)

if(df < 0):
    df = 0

df = df.astype('str')

# print the results
print("Your safety score is: " + df, PendingDeprecationWarning)

# plot the data
plt.figure()
plt.plot(user_data[:, 0], user_data[:, 1])
plt.plot(optimal_data[:, 0], optimal_data[:, 1])
plt.show()

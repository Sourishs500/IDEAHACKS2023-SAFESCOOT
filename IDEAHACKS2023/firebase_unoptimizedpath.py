from firebase import Firebase
import numpy as np
import matplotlib.pyplot as plt
import time

#userfile = open(r"routedata.txt", "w")

config = {
  "apiKey": "AIzaSyD3Zd2-L7svnWHd1bRxe1AgfjUaUA3f9DA",
  "authDomain": "safescoot-8d212.firebaseapp.com",
  "databaseURL": "https://safescoot-8d212-default-rtdb.firebaseio.com/",
  "storageBucket": "safescoot-8d212.appspot.com"
}

firebase = Firebase(config)

# Get a reference to the auth service
auth = firebase.auth()

# Get a reference to the database service
db = firebase.database()

coordinates = db.child("test").get()
start = time.time()
current = ""
print(coordinates.val())

"""
def reading():
    for key, value in coordinates.val().items():
        userfile.write(str(value) + " ")
        print(coordinates.val())
        #current = str(value)
        #start = time.time()

while(True):
    reading()
    time.sleep(2)
"""
badRoute = []
i = 0
while (len(badRoute) < 50):
    for key, value in coordinates.val().items():
        badRoute[i] = value
        i = i+1
        print(coordinates.val())
        time.sleep(3)


"""
while(True):
    with open("routedata.txt", mode="wt") as f:
        for key, value in coordinates.val().items():
            f.write(str(value) + " ")
            print(coordinates.val())
        f.write("\n")
    f.close()
"""
"""
for key, value in coordinates.val().items():
    x,y=np.loadtxt("userroutedata.txt",unpack=True)
    plt.plot(x,y)

plt.show()
"""

print(badRoute)
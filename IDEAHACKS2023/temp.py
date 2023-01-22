import osmnx as ox
import requests as r
import json
import numpy as np

#optimizedfile = open(r"oppath.txt", "w+")



result =r.get('https://router.project-osrm.org/route/v1/driving/-118.455028,34.070308;-118.455429,34.074674?alternatives=false&annotations=nodes')

"""
result2 = r.get('https://api.openstreetmap.org/api/0.6/node/1457413462', timeout = 1)
print(result2.text)
"""
#print(result.text)

#y2 = result.json()

#print(result.json())

#y = json.loads(result.text)


y3 = result.text

#print(y2['routes'])

indexBegin = y3.find("nodes")
#print(indexBegin)

indexEnd = y3.find("distance")
#print(indexEnd)

s = ""

#print(len(y3))
i = indexBegin+8
while i < indexEnd - 4:
    s += y3[i]
    i = i + 1
    
print(s)

f_nodes = s.split(',')
print(f_nodes)

result3 = []
api_statement = "https://api.openstreetmap.org/api/0.6/node/"

for x in f_nodes:
    a = r.get(api_statement + x, timeout=1)
    result3.append(a.text)
    

#print(result3)

count = len(result3)
i2 = 0 
sLat = ""
sLon = ""
w, h = 2, count
f_array = [[0 for x in range(w)] for y in range(h)] 
while i2 < count:
    sLat = ""
    sLon = ""
    indexBeginLat = result3[i2].find("lat=")
    indexEndLat = result3[i2].find(" lon")
    #print(indexBeginLat)
    #print(indexEndLat)
    iLat = indexBeginLat+5
    while iLat < indexEndLat-1:
        sLat += result3[i2][iLat]
        iLat = iLat+1
    indexBeginLon = result3[i2].find("lon=")
    if(result3[i2][indexBeginLon:].find("<tag") > 0):
        indexEndLon = -1 + len(result3[i2][:indexBeginLon]) + result3[i2][indexBeginLon:].find(">")
        #print(indexEndLon)
    else:
        indexEndLon = result3[i2].find("\"/>")
    iLon = indexBeginLon+5
    #sLon = result3[i2][indexBeginLon:indexEndLon]
    while iLon < indexEndLon:
        sLon += result3[i2][iLon]
        iLon = iLon+1
    f_array[i2][0] = sLat
    f_array[i2][1] = sLon
    i2 = i2+1
    
print(f_array)


lat = []
lon = []
    
#print(f_array[i3][0]+f_array[i3][1])


for b in f_array:
    lat.append(float(b[0]))
    lon.append(float(b[1]))
    
f_lat = np.array(lat)
f_lon = np.array(lon)
f_coords = np.dstack((f_lat, f_lon))

    
with open ('oppath.txt', 'w') as file:
    file.write(str(f_coords))
    


    
    
    
    
    
    
    



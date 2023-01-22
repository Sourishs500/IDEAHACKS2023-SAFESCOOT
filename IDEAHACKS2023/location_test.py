import osmnx as ox

G = ox.graph_from_place('Piedmont, CA, USA', network_type='drive')
node_id = list(G.nodes)[0]
print(G.nodes[node_id]['x']) #lon
print(G.nodes[node_id]['y']) #lat


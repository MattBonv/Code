import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_shortest_path(graph, start, end):
    shortest_paths = nx.shortest_path(graph, source=start, weight='distance')
    shortest_path = shortest_paths[end]

    total_distance = sum(graph[shortest_path[i]][shortest_path[i+1]]['distance'] for i in range(len(shortest_path) - 1))

    return shortest_path, total_distance


def dijkstra_fastest_path(graph, start, end):
    shortest_paths = nx.shortest_path(graph, source=start, weight='time')
    shortest_path = shortest_paths[end]

    total_distance = sum(graph[shortest_path[i]][shortest_path[i+1]]['time'] for i in range(len(shortest_path) - 1))

    return shortest_path, total_distance



#undirected graph
G = nx.Graph()  

# Here is the database with distance and time (I dont take road types yet)
edges = [
    ("Minfeng", "Qiao mo", {'distance': 300, 'time': 180}), 
    ("Qiao mo", "Minfeng", {'distance': 300, 'time': 180}),  
    ("Yutian", "Minfeng", {'distance': 110, 'time': 105}),  
    ("Minfeng", "Yutian", {'distance': 110, 'time': 105}),  
    ("Minfeng", "Luntai", {'distance': 575, 'time': 390}),
    ("Luntai", "Minfeng", {'distance': 575, 'time': 390}),  
    ("Luntai", "Korler/Korla", {'distance': 176, 'time': 105}),
    ("Korler/Korla", "Luntai", {'distance': 176, 'time': 105}),  
    ("Kuqa", "Luntai", {'distance': 115, 'time': 75}),
    ("Luntai", "Kuqa", {'distance': 115, 'time': 75}),  
    ("Aksu", "Kuqa", {'distance': 346, 'time': 240}),
    ("Kuqa", "Aksu", {'distance': 346, 'time': 240}),  
    ("Atushi / Atux", "Aksu", {'distance': 426, 'time': 240}),
    ("Aksu", "Atushi / Atux", {'distance': 426, 'time': 240}),  
    ("Kashgar / Kashi", "Atushi / Atux", {'distance': 47, 'time': 30}),
    ("Atushi / Atux", "Kashgar / Kashi", {'distance': 47, 'time': 30}),  
    ("Taxkorgan", "Kashgar / Kashi", {'distance': 290, 'time': 195}),
    ("Kashgar / Kashi", "Taxkorgan", {'distance': 290, 'time': 195}),  
    ("Yarkland", "Hotan", {'distance': 315, 'time': 225}),
    ("Hotan", "Yarkland", {'distance': 315, 'time': 225}),  
    ("Yarkland", "Kashgar / Kashi", {'distance': 190, 'time': 150}),
    ("Kashgar / Kashi", "Yarkland", {'distance': 190, 'time': 150}),  
    ("Hotan", "Yutian", {'distance': 201, 'time': 220}),
    ("Yutian", "Hotan", {'distance': 201, 'time': 220}),  
    ("Qiao mo", "Ruoqiang", {'distance': 306, 'time': 180}),
    ("Ruoqiang", "Qiao mo", {'distance': 306, 'time': 180}),  
    ("Ruoqiang", "Korler/Korla", {'distance': 437, 'time': 255}),
    ("Korler/Korla", "Ruoqiang", {'distance': 437, 'time': 255}),  
    ("Kuqa", "Xinyuan", {'distance': 505, 'time': 360}),
    ("Xinyuan", "Kuqa", {'distance': 505, 'time': 360}),  
    ("Korler/Korla", "Kuitun / Kuytun", {'distance': 740, 'time': 525}),
    ("Kuitun / Kuytun", "Korler/Korla", {'distance': 740, 'time': 525}),  
    ("Xinyuan", "Kuitun / Kuytun", {'distance': 290, 'time': 225}),
    ("Kuitun / Kuytun", "Xinyuan", {'distance': 290, 'time': 225}),  
    ("Xinyuan", "Urumqi", {'distance': 518, 'time': 360}),
    ("Urumqi", "Xinyuan", {'distance': 518, 'time': 360}),  
    ("Korler/Korla", "Urumqi", {'distance': 381, 'time': 270}),
    ("Urumqi", "Korler/Korla", {'distance': 381, 'time': 270}),  
    ("Kuitun / Kuytun", "Urumqi", {'distance': 240, 'time': 135}),
    ("Urumqi", "Kuitun / Kuytun", {'distance': 240, 'time': 135}),  
    ("Kuitun / Kuytun", "Karamay", {'distance': 154, 'time': 105}),
    ("Karamay", "Kuitun / Kuytun", {'distance': 154, 'time': 105}),  
    ("Karamay", "Urumqi", {'distance': 389, 'time': 210}),
    ("Urumqi", "Karamay", {'distance': 389, 'time': 210}),  
    ("Korler/Korla", "Turpan", {'distance': 362, 'time': 345}),
    ("Turpan", "Korler/Korla", {'distance': 362, 'time': 345}),  
    ("Turpan", "Urumqi", {'distance': 210, 'time': 225}),
    ("Urumqi", "Turpan",{'distance': 210, 'time': 225}),  
    ("Hotan", "Alaer/Aral", {'distance': 438, 'time': 300}),
    ("Alaer/Aral", "Hotan", {'distance': 438, 'time': 300}),  
    ("Alaer/Aral", "Kuqa", {'distance': 230, 'time': 165}),
    ("Kuqa", "Alaer/Aral", {'distance': 230, 'time': 165}),  
    ("Kuqa", "Yili/Yining", {'distance': 590, 'time': 360}),
    ("Yili/Yining", "Kuqa", {'distance': 590, 'time': 360}),  
    ("Yili/Yining", "Xinyuan", {'distance': 184, 'time': 105}),
    ("Xinyuan", "Yili/Yining", {'distance': 184, 'time': 105}),  
]

G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42) 
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_weight='bold')

# Add weight labels on edges
labels = {(u, v): f"{data['distance']}km\n{data['time']}min" for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Use the dijkstra to calculate shortest path
start_node = "Minfeng"
end_node = "Karamay"
shortest_path, total_distance = dijkstra_shortest_path(G, start_node, end_node)

# Highlight the shortest path in red
node_colors = ['red' if node in shortest_path else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1000)
nx.draw_networkx_labels(G, pos)
edge_colors = ['red' if (u, v) in zip(shortest_path, shortest_path[1:]) else 'black' for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)

# Print the shortest path and distance
print("Shortest path:", shortest_path)  
print("Total distance:", total_distance, "km")

plt.show()
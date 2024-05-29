import networkx as nx
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, StringVar, Listbox, END, MULTIPLE, OptionMenu

def dijkstra_shortest_path(graph, start, end):
    shortest_paths = nx.shortest_path(graph, source=start, weight='distance')
    shortest_path = shortest_paths[end]

    total_distance = sum(graph[shortest_path[i]][shortest_path[i+1]]['distance'] for i in range(len(shortest_path) - 1))

    return shortest_path, total_distance

def create_custom_route(graph, start, end, waypoints):
    total_path = []
    total_distance = 0

    # Initial starting point
    current_start = start

    for waypoint in waypoints:
        path_segment, distance_segment = dijkstra_shortest_path(graph, current_start, waypoint)
        total_path += path_segment[:-1]  # Add path segment, except the last node to avoid duplication
        total_distance += distance_segment
        current_start = waypoint

    # Final segment to the destination
    path_segment, distance_segment = dijkstra_shortest_path(graph, current_start, end)
    total_path += path_segment
    total_distance += distance_segment

    return total_path, total_distance

def draw_graph(G, shortest_path, custom_path):
    plt.figure(figsize=(14, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_weight='bold')

    labels = {(u, v): f"{data['distance']}km\n{data['time']}min" for u, v, data in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Highlight the custom path in green first
    green_edges = list(zip(custom_path, custom_path[1:]))
    edge_colors = ['green' if edge in green_edges or (edge[1], edge[0]) in green_edges else 'black' for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)

    # Highlight the shortest path in red after the green path
    red_edges = list(zip(shortest_path, shortest_path[1:]))
    edge_colors = ['red' if edge in red_edges or (edge[1], edge[0]) in red_edges else edge_colors[i] for i, edge in enumerate(G.edges())]
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)

    plt.show()

def on_calculate():
    start_node = start_var.get()
    end_node = end_var.get()
    waypoints = [waypoint_listbox.get(i) for i in waypoint_listbox.curselection()]

    shortest_path, total_distance = dijkstra_shortest_path(G, start_node, end_node)
    custom_path, custom_distance = create_custom_route(G, start_node, end_node, waypoints)

    shortest_path_text.set(f"Shortest Path (Red): {' -> '.join(shortest_path)}\nTotal distance: {total_distance} km")
    custom_path_text.set(f"Custom Path (Green): {' -> '.join(custom_path)}\nTotal distance: {custom_distance} km")

    draw_graph(G, shortest_path, custom_path)

# undirected graph
G = nx.Graph()

edges = [
    ("Minfeng", "Qiao mo", {'distance': 300, 'time': 180}), 
    ("Yutian", "Minfeng", {'distance': 110, 'time': 105}),  
    ("Minfeng", "Luntai", {'distance': 575, 'time': 390}),
    ("Luntai", "Korler/Korla", {'distance': 176, 'time': 105}),
    ("Kuqa", "Luntai", {'distance': 115, 'time': 75}),  
    ("Aksu", "Kuqa", {'distance': 346, 'time': 240}),
    ("Atushi / Atux", "Aksu", {'distance': 426, 'time': 240}),  
    ("Kashgar / Kashi", "Atushi / Atux", {'distance': 47, 'time': 30}),  
    ("Taxkorgan", "Kashgar / Kashi", {'distance': 290, 'time': 195}),  
    ("Yarkland", "Hotan", {'distance': 315, 'time': 225}),  
    ("Yarkland", "Kashgar / Kashi", {'distance': 190, 'time': 150}),  
    ("Hotan", "Yutian", {'distance': 201, 'time': 220}),  
    ("Qiao mo", "Ruoqiang", {'distance': 306, 'time': 180}),  
    ("Ruoqiang", "Korler/Korla", {'distance': 437, 'time': 255}),  
    ("Kuqa", "Xinyuan", {'distance': 505, 'time': 360}),  
    ("Korler/Korla", "Kuitun / Kuytun", {'distance': 740, 'time': 525}),  
    ("Xinyuan", "Kuitun / Kuytun", {'distance': 290, 'time': 225}),  
    ("Xinyuan", "Urumqi", {'distance': 518, 'time': 360}),  
    ("Korler/Korla", "Urumqi", {'distance': 381, 'time': 270}),  
    ("Kuitun / Kuytun", "Urumqi", {'distance': 240, 'time': 135}),  
    ("Kuitun / Kuytun", "Karamay", {'distance': 154, 'time': 105}),  
    ("Karamay", "Urumqi", {'distance': 389, 'time': 210}),  
    ("Korler/Korla", "Turpan", {'distance': 362, 'time': 345}),  
    ("Turpan", "Urumqi", {'distance': 210, 'time': 225}),  
    ("Hotan", "Alaer/Aral", {'distance': 438, 'time': 300}),  
    ("Alaer/Aral", "Kuqa", {'distance': 230, 'time': 165}),  
    ("Kuqa", "Yili/Yining", {'distance': 590, 'time': 360}),  
    ("Yili/Yining", "Xinyuan", {'distance': 184, 'time': 105}),  
]

G.add_edges_from(edges)

# Set up the Tkinter interface
root = Tk()
root.title("Personnalised.Itinary")

# Set the window size to a large dimension
window_width = 1200
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

Label(root, text="Starting Point:").grid(row=0, column=0, padx=10, pady=10)
start_var = StringVar()
start_menu = OptionMenu(root, start_var, *G.nodes())
start_menu.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Arriving Point:").grid(row=1, column=0, padx=10, pady=10)
end_var = StringVar()
end_menu = OptionMenu(root, end_var, *G.nodes())
end_menu.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Intermedary Points:").grid(row=2, column=0, padx=10, pady=10)
waypoint_listbox = Listbox(root, selectmode=MULTIPLE, height=10, width=30)
waypoint_listbox.grid(row=2, column=1, padx=10, pady=10)
for node in G.nodes():
    waypoint_listbox.insert(END, node)

Button(root, text="Calculate Itinary", command=on_calculate).grid(row=3, column=1, padx=10, pady=10)

# Text variables for displaying the paths
shortest_path_text = StringVar()
custom_path_text = StringVar()

Label(root, textvariable=shortest_path_text, fg='red', wraplength=1000).grid(row=4, column=0, columnspan=2, sticky='w', padx=10, pady=10)
Label(root, textvariable=custom_path_text, fg='green', wraplength=1000).grid(row=5, column=0, columnspan=2, sticky='w', padx=10, pady=10)

root.mainloop()

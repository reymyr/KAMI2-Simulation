import networkx as nx
import matplotlib.pyplot as plt

# Create the graph
G = nx.Graph()
G.add_nodes_from([
    (1, {"color": "green"}),
    (2, {"color": "blue"}),
    (3, {"color": "orange"}),
    (4, {"color": "green"}),
    (5, {"color": "orange"}),
    (6, {"color": "orange"}),
    (7, {"color": "orange"}),
    (8, {"color": "blue"}),
    (9, {"color": "blue"}),
    (10, {"color": "green"}),
    (11, {"color": "green"}),
    (12, {"color": "green"}),
    (13, {"color": "orange"})
])
G.add_edges_from([
    (1, 2),
    (1, 3),
    (1, 9),
    (3, 4),
    (4, 5),
    (4, 6),
    (4, 7),
    (5, 8),
    (6, 8),
    (7, 8),
    (9, 10),
    (9, 11),
    (9, 12),
    (10, 13),
    (11, 13),
    (12, 13)
])

# Get all the colors in the graph
colors = set(nx.get_node_attributes(G, "color").values())

# Function to color a vertex and all of the connected 
# vertex that have the same color using DFS
def colorNode(G, id, color, visited):
    if id not in visited:
        old_color = G.nodes[id]["color"]
        G.nodes[id]["color"] = color
        visited.append(id)

        neighbor = nx.neighbors(G, id)
        for n in neighbor:
            if G.nodes[n]["color"] == old_color:
                colorNode(G, n, color, visited)

# Function to draw the graph
def drawGraph(G):
    color = [G.nodes[i]["color"] for i in G]
    pos = nx.planar_layout(G)
    nx.draw(G, pos, node_color=color, with_labels=True)
    plt.show(block=False)


drawGraph(G)
win = False
moves = 0
while not win:
    # Get the player command
    print("Enter node to color in the format 'node_number color': ")
    command = input()

    if command == "exit":
        break

    if len(command.split()) == 2 and command.split()[1] in colors:
        moves += 1
        nId = int(command.split()[0])
        color = command.split()[1]
        colorNode(G, nId, color, [])
        drawGraph(G)

        # Win condition checking
        if len(set(nx.get_node_attributes(G, "color").values())) == 1:
            win = True
    else:
        print("Invalid input")

# Winning message
if win:
    print("You won with", moves, "moves")
    input()

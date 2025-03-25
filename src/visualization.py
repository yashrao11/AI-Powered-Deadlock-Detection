from pyvis.network import Network
import networkx as nx

def visualize_interactive_rag(graph, deadlock_cycle=None):
    net = Network(notebook=False, height="500px", width="100%", bgcolor="#222222", font_color="white")
    
    # Add nodes and edges
    for node in graph.nodes:
        color = "lightblue" if node.startswith("P") else "lightcoral"
        net.add_node(node, label=node, color=color)

    for edge in graph.edges:
        net.add_edge(edge[0], edge[1])

    # Highlight deadlock cycle (if any)
    if deadlock_cycle:
        for i in range(len(deadlock_cycle)):
            net.add_edge(deadlock_cycle[i], deadlock_cycle[(i + 1) % len(deadlock_cycle)], color="red", width=3)

    net.show("templates/interactive_graph.html")

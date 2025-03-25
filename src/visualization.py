import matplotlib.pyplot as plt
import networkx as nx

def visualize_rag(graph, deadlock_cycle=None):
    """Visualizes the Resource Allocation Graph with deadlocks highlighted."""
    pos = nx.spring_layout(graph)

    # Draw all nodes
    nx.draw(graph, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10)

    # Highlight deadlock nodes if a cycle exists
    if deadlock_cycle:
        deadlock_nodes = set(node for edge in deadlock_cycle for node in edge[:2])
        nx.draw_networkx_nodes(graph, pos, nodelist=deadlock_nodes, node_color="red")

    plt.show()

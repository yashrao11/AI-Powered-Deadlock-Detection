import matplotlib.pyplot as plt
import networkx as nx

def visualize_deadlock(graph):
    pos = nx.spring_layout(graph)  # Or any other layout for visualization
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10)
    plt.show(block=False)  # Show plot without blocking execution

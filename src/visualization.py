import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def draw_graph(edges):
    """Creates and returns an HTML image of the graph."""
    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    plt.figure(figsize=(6, 6))
    nx.draw(graph, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    return f'<img src="data:image/png;base64,{encoded_image}"/>'

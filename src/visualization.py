from pyvis.network import Network
import networkx as nx

def draw_graph(graph_edges, output_html="graph.html"):
    """
    Draws a directed graph using Pyvis and saves it as an HTML file.

    :param graph_edges: List of tuples representing edges in the graph.
    :param output_html: Output file name (default: 'graph.html').
    """
    G = nx.DiGraph()

    # Add edges
    for edge in graph_edges:
        G.add_edge(edge[0], edge[1])

    net = Network(height="500px", width="100%", directed=True)
    net.from_nx(G)
    net.show(output_html)

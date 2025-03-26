from pyvis.network import Network
import networkx as nx
import streamlit as st
import tempfile
import os

def draw_graph(edges):
    """
    Draws a process-resource graph and displays it in Streamlit.

    :param edges: List of tuples representing process-resource relationships.
    """
    try:
        # Ensure Pyvis is correctly initialized
        net = Network(directed=True, notebook=False, height="500px", width="100%")
        
        # Create a directed graph using NetworkX
        graph = nx.DiGraph()
        graph.add_edges_from(edges)

        # Add nodes and edges to Pyvis
        for node in graph.nodes:
            net.add_node(node, label=node)

        for edge in graph.edges:
            net.add_edge(edge[0], edge[1])

        # Ensure output directory exists
        output_dir = "graphs"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the graph to a temporary HTML file
        temp_file_path = os.path.join(output_dir, "graph.html")
        net.save_graph(temp_file_path)

        # Display the graph in Streamlit
        with open(temp_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
            st.components.v1.html(html_content, height=500, scrolling=True)

    except Exception as e:
        st.error(f"An error occurred while rendering the graph: {e}")

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import ast
from src.deadlock import detect_deadlock  # Import your deadlock detection logic

# Function to visualize graph
def visualize_graph(graph, cycle):
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, edge_color="gray")

    if cycle:
        nx.draw_networkx_edges(graph, pos, edgelist=cycle, edge_color="red", width=2)
    
    st.pyplot(plt)

# Streamlit UI
st.title("🔍 AI-Powered Deadlock Detector")

graph_input = st.text_area("Enter Resource Allocation Graph (RAG) as Python List of Tuples:", "[('P1', 'R1'), ('R1', 'P2'), ('P2', 'R2'), ('R2', 'P3'), ('P3', 'R1')]")

if st.button("Detect Deadlock"):
    try:
        edges = ast.literal_eval(graph_input)
        G = nx.DiGraph()
        G.add_edges_from(edges)

        deadlock_cycle = detect_deadlock(G)

        if deadlock_cycle:
            st.error(f"🔴 Deadlock Detected! Cycle: {deadlock_cycle}")
        else:
            st.success("✅ No Deadlock Detected.")

        visualize_graph(G, deadlock_cycle)

    except Exception as e:
        st.error(f"Invalid input: {e}")

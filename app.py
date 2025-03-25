import streamlit as st
import networkx as nx
import ast
import sys
import os

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath("src"))

# Import custom functions from src
from deadlock import detect_deadlock
from visualization import visualize_rag

# Streamlit UI
st.title("🔍 AI-Powered Deadlock Detection System")

st.write("Enter the Resource Allocation Graph (RAG) as a list of edges:")

# User input
graph_input = st.text_area("Example: [('P1', 'R1'), ('R1', 'P2'), ('P2', 'R2')]")

if st.button("Detect Deadlock"):
    try:
        # Convert input string to actual list of edges
        graph_edges = ast.literal_eval(graph_input)

        # Create directed graph
        G = nx.DiGraph()
        G.add_edges_from(graph_edges)

        # Detect deadlock
        deadlock_cycle = detect_deadlock(G)

        # Show result
        if deadlock_cycle:
            st.error(f"🔴 Deadlock detected! Cycle: {deadlock_cycle}")
        else:
            st.success("✅ No deadlock detected.")

        # Visualize RAG
        visualize_rag(G, deadlock_cycle)

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

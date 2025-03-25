import streamlit as st
import networkx as nx
import json
from src.deadlock import detect_deadlock, suggest_deadlock_solution
from src.visualization import visualize_interactive_rag
import sys
import os

sys.path.append(os.path.abspath("src"))
from src.deadlock import detect_deadlock, suggest_deadlock_solution

# Predefined graphs for quick testing
predefined_graphs = {
    "No Deadlock": [("P1", "R1"), ("R1", "P2"), ("P2", "R3")],
    "Deadlock Example": [("P1", "R1"), ("R1", "P2"), ("P2", "R2"), ("R2", "P3"), ("P3", "R1")],
    "Complex Deadlock": [("P1", "R1"), ("P2", "R2"), ("R1", "P2"), ("R2", "P1")]
}

# Streamlit UI Setup
st.set_page_config(page_title="AI-Powered Deadlock Detection", layout="wide")

st.title("🔍 AI-Powered Deadlock Detection")
st.write("An interactive tool to visualize and detect deadlocks in resource allocation graphs.")

# Sidebar for Graph Input
st.sidebar.header("Graph Input Options")
selected_graph = st.sidebar.selectbox("Select a predefined scenario:", list(predefined_graphs.keys()))
graph_edges = predefined_graphs[selected_graph]

# Create Graph
G = nx.DiGraph()
G.add_edges_from(graph_edges)

# Detect Deadlock
deadlock_cycle = detect_deadlock(G)

# Show Results
st.subheader("🛠 Deadlock Detection Result")
if deadlock_cycle:
    st.error(f"🔴 Deadlock Detected! Cycle: {deadlock_cycle}")
    suggestion = suggest_deadlock_solution(deadlock_cycle)
    st.warning(f"💡 Suggested Fix: {suggestion}")
else:
    st.success("✅ No Deadlock Detected.")

# Show Interactive Graph
st.subheader("📊 Resource Allocation Graph")
visualize_interactive_rag(G, deadlock_cycle)
st.components.v1.html(open("templates/interactive_graph.html", "r").read(), height=550)

# Graph Export & Sharing
graph_json = json.dumps(graph_edges)
st.download_button("📥 Download Graph", graph_json, "graph.json", "application/json")

shareable_link = f"https://ai-powered-deadlock-detection.app/?graph={graph_json}"
st.markdown(f"🔗 **[Share this Graph]({shareable_link})**", unsafe_allow_html=True)

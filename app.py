import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import ast
import os
import sys

# Ensure src module is accessible
sys.path.append(os.path.abspath("src"))

# Import deadlock detection functions
from src.deadlock import detect_deadlock, suggest_deadlock_solution
from src.visualization import draw_graph

# Streamlit UI
st.title("🔗 AI-Powered Deadlock Detection System")

st.markdown("""
### 🎯 **How to Use:**
1. **Enter the Graph Edges** as a list of tuples, e.g., `[("P1", "R1"), ("R1", "P2"), ("P2", "R3")]`
2. **Click "Detect Deadlock"** to analyze the resource allocation.
3. **View Results** - The system will check for deadlock & suggest fixes.
4. **Visualize Graph** - See how processes & resources interact.
""")

# User input for resource allocation graph
graph_input = st.text_area("📝 Enter Graph Edges:", "[('P1', 'R1'), ('R1', 'P2'), ('P2', 'R3')]")

# Convert input to list of tuples
try:
    graph_edges = ast.literal_eval(graph_input)
    if not isinstance(graph_edges, list) or not all(isinstance(edge, tuple) and len(edge) == 2 for edge in graph_edges):
        st.error("⚠️ Invalid input format! Enter a list of (Process, Resource) tuples.")
        st.stop()
except Exception:
    st.error("⚠️ Could not parse input. Ensure it's a valid list of tuples.")
    st.stop()

# Button to detect deadlock
if st.button("🚀 Detect Deadlock"):
    deadlock_detected, cycle = detect_deadlock(graph_edges)

    if deadlock_detected:
        st.error(f"❌ Deadlock detected! 🔄 Cycle: {cycle}")

        # Suggest solution
        solution = suggest_deadlock_solution(graph_edges)
        if solution:
            st.success(f"💡 Suggested Fix: {solution}")
        else:
            st.warning("⚠️ No automatic fix available. Consider modifying the graph manually.")
    else:
        st.success("✅ No deadlock detected.")

    # Visualize Graph
    st.subheader("📊 Resource Allocation Graph")
    draw_graph(graph_edges)

# Footer
st.markdown("---")
st.markdown("👨‍💻 Developed by [Your Name] | 🔗 [GitHub](https://github.com/your-repo)")

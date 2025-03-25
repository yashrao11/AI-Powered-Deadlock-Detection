import sys
import os
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Ensure the 'src' directory is in the Python path
sys.path.append(os.path.abspath("src"))

try:
    from deadlock import detect_deadlock, suggest_deadlock_solution
except ImportError:
    st.error("⚠️ ImportError: Could not import 'deadlock.py' from 'src/'. Ensure the file exists and is correctly structured.")
    sys.exit(1)

# Streamlit UI
st.title("🔍 AI-Powered Deadlock Detection")

st.write("""
### How It Works:
- Enter the processes and resources.
- The system will analyze for deadlocks.
- If a deadlock is found, it will suggest possible solutions.
""")

# User Input
st.subheader("➕ Enter Edges (Process → Resource or Resource → Process)")
edges_input = st.text_area("Enter edges as comma-separated tuples", "('P1', 'R1'), ('R1', 'P2'), ('P2', 'R3')")

if st.button("Detect Deadlock"):
    try:
        # Convert input string to a list of tuples
        edges = eval(f"[{edges_input}]")  # Safe conversion
        
        # Create a directed graph
        G = nx.DiGraph()
        G.add_edges_from(edges)

        # Detect deadlock
        deadlock_cycle = detect_deadlock(G)

        if deadlock_cycle:
            st.error(f"🚨 Deadlock Detected! Cycle: {deadlock_cycle}")
            
            # Suggest solution
            fix_suggestion = suggest_deadlock_solution(G, deadlock_cycle)
            st.warning(f"🛠 Suggested Fix: {fix_suggestion}")
        else:
            st.success("✅ No Deadlock Detected!")

        # Visualizing the graph
        st.subheader("🔗 Resource Allocation Graph")
        plt.figure(figsize=(8, 5))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=12, edge_color="gray")
        st.pyplot(plt)

    except Exception as e:
        st.error(f"❌ Error: {e}")


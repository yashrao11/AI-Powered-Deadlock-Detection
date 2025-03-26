import sys
import os
import streamlit as st
import streamlit.components.v1 as components

# Manually set the correct path for src
SRC_DIR = r"C:\Users\DC\Desktop\ONgoing Stuff\CSE316 - OPERATING SYSTEMS\PROJECT\AI-Powered-Deadlock-Detection\src"
sys.path.append(SRC_DIR)  # Add src to Python path

# Now import modules
try:
    from deadlock import detect_all_deadlocks
    from visualization import draw_graph
except ImportError as e:
    st.error(f"🚨 Import Error: {e}\n❌ Check if 'src/' exists and contains 'deadlock.py'.")
    st.stop()

def parse_edges(edges_input):
    """Parses input edges in both 'A B, B C' and 'AB, BC' formats."""
    edges = []
    for edge in edges_input.split(","):
        edge = edge.strip()
        if " " in edge:
            nodes = edge.split()  # Handles 'A B' format
        else:
            nodes = [edge[:len(edge)//2], edge[len(edge)//2:]]  # Handles 'AB' format
        
        if len(nodes) == 2 and nodes[0] and nodes[1]:
            edges.append(tuple(nodes))
    
    return edges

def main():
    st.title("🛠️ AI-Powered Deadlock Detection")

    st.write("### Enter process-resource relationships:")
    edges_input = st.text_input("Enter edges (format: 'P1 R1, P2 R2' or 'P1R1, P2R2')", "")

    if st.button("Detect Deadlocks"):
        if not edges_input.strip():
            st.error("❌ Please enter at least one process-resource relationship.")
            return
        
        try:
            edges = parse_edges(edges_input)
            if not edges:
                st.error("❌ Invalid input. Please enter valid process-resource relationships.")
                return
        except Exception:
            st.error("❌ Invalid input format. Please enter in the correct format.")
            return

        # Detect Deadlocks
        deadlocks = detect_all_deadlocks(edges)

        if deadlocks:
            st.error(f"⚠️ Deadlocks detected! {len(deadlocks)} cycles found:")
            for i, cycle in enumerate(deadlocks, 1):
                st.write(f"🔴 Cycle {i}: {cycle}")
        else:
            st.success("✅ No deadlocks detected")

        # Render Graph
        try:
            output_html = draw_graph(edges)
            components.html(output_html, height=600, scrolling=True)
        except Exception as e:
            st.error(f"❌ An error occurred while rendering the graph: {e}")

if __name__ == "__main__":
    main()

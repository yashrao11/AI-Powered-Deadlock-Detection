import streamlit as st
import networkx as nx
from src.deadlock import detect_deadlock
from src.visualization import draw_graph

def parse_edges(edges_input):
    """Parses input edges in both 'a b, b c' and 'ab, bc' formats."""
    edges = []
    for edge in edges_input.split(","):
        edge = edge.strip()
        if " " in edge:
            nodes = edge.split()  # Handles 'a b' format
        else:
            nodes = [edge[:len(edge)//2], edge[len(edge)//2:]]  # Handles 'ab' format
        
        if len(nodes) == 2 and nodes[0] and nodes[1]:
            edges.append(tuple(nodes))
    
    return edges

def main():
    st.title("🛠️ AI-Powered Deadlock Detection")

    st.write("### Enter process-resource relationships:")
    edges_input = st.text_input("Enter edges (format: 'P1 R1, P2 R2' or 'P1R1, P2R2')", "")

    if st.button("Detect Deadlock"):
        if not edges_input.strip():
            st.error("Please enter at least one process-resource relationship.")
            return
        
        try:
            edges = parse_edges(edges_input)
            if not edges:
                st.error("Invalid input. Please enter valid process-resource relationships.")
                return
        except Exception:
            st.error("Invalid input format. Please enter in the correct format.")
            return

        # Detect Deadlock
        deadlock_detected, cycles = detect_deadlock(edges)

        if deadlock_detected:
            st.error(f"⚠️ Deadlock detected! Cycle found: {cycles}")
        else:
            st.success("✅ No deadlock detected")

        # Render Graph
        try:
            output_html = draw_graph(edges)
            st.components.v1.html(output_html, height=600, scrolling=True)
        except Exception as e:
            st.error(f"An error occurred while rendering the graph: {e}")

if __name__ == "__main__":
    main()

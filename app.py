import streamlit as st
import networkx as nx
from src.deadlock import detect_deadlock, suggest_deadlock_solution
from src.visualization import draw_graph

def parse_edges(edges_input):
    """Parses input edges in both 'a b, b c' and 'ab, bc' formats."""
    edges = []
    # Remove newlines and split by comma
    for edge in edges_input.replace("\n", "").split(","):
        edge = edge.strip()
        if not edge:
            continue
        if " " in edge:
            nodes = edge.split()  # Handles 'a b' format
        else:
            # If no space, assume the first half is the first node and the rest is the second node.
            mid = len(edge) // 2
            nodes = [edge[:mid], edge[mid:]]
        if len(nodes) == 2 and nodes[0] and nodes[1]:
            edges.append(tuple(nodes))
    return edges

def main():
    st.title("🛠️ AI-Powered Deadlock Detection")
    st.write("### Enter process-resource relationships:")

    edges_input = st.text_area("Enter edges (format: 'P1 R1, P2 R2' or 'P1R1, P2R2')", height=200)

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

        # Detect deadlock
        deadlock_detected, cycles = detect_deadlock(edges)

        if deadlock_detected:
            st.error("⚠️ Deadlock detected!")
            # Display each cycle
            for idx, cycle in enumerate(cycles, start=1):
                st.write(f"Cycle {idx}: {cycle}")
            # Optionally, display a suggestion for resolution
            suggestion = suggest_deadlock_solution(cycles)
            if suggestion:
                st.info(f"Suggested Fix: {suggestion}")
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

import streamlit as st
import networkx as nx
from src.deadlock import detect_deadlock
from src.visualization import draw_graph

def main():
    st.title("🛠️ AI-Powered Deadlock Detection")

    st.write("### Enter process-resource relationships:")
    edges_input = st.text_input("Enter edges (format: P1 R1, P2 R2, ...)", "")

    if st.button("Detect Deadlock"):
        if not edges_input.strip():
            st.error("Please enter at least one process-resource relationship.")
            return
        
        # Process input
        try:
            edges = [tuple(edge.strip().split()) for edge in edges_input.split(",")]
        except Exception:
            st.error("Invalid input format. Please enter in the correct format: P1 R1, P2 R2, ...")
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

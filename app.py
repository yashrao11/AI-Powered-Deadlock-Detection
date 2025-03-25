import streamlit as st
from src.visualization import draw_graph
from src.deadlock import detect_deadlock, suggest_deadlock_solution

def main():
    st.title("AI-Powered Deadlock Detection")

    st.write("Enter process-resource relationships:")
    
    input_text = st.text_area("Enter edges (format: P1 R1, P2 R2, P2 R1, ...)", "")

    if st.button("Detect Deadlock"):
        edges = [tuple(edge.strip().split()) for edge in input_text.split(",") if edge.strip()]
        
        if not edges:
            st.error("Please enter valid edges!")
            return

        deadlock_detected, cycles = detect_deadlock(edges)

        if deadlock_detected:
            st.error("Deadlock detected! 🔴")
            st.write(f"Cycles: {cycles}")
            st.write("Suggested solutions:")
            st.write(suggest_deadlock_solution(cycles))
        else:
            st.success("No deadlock detected ✅")

        draw_graph(edges)

if __name__ == "__main__":
    main()

from streamlit_drawable_canvas import st_canvas
import streamlit as st
import networkx as nx

class CanvasEditor:
    def __init__(self):
        self.canvas_width = 600
        self.canvas_height = 400
        
    def get_edges(self):
        st.write("Draw nodes and edges:")
        
        # Create canvas
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=2,
            stroke_color="#000000",
            background_color="#FFFFFF",
            width=self.canvas_width,
            height=self.canvas_height,
            drawing_mode="freedraw",
            key="canvas"
        )
        
        # Process drawing into edges
        if canvas_result.json_data is not None:
            objects = canvas_result.json_data["objects"]
            nodes = set()
            edges = []
            
            for obj in objects:
                if obj["type"] == "rect":
                    nodes.add(f"P{obj['left']//100}")
                elif obj["type"] == "circle":
                    nodes.add(f"R{obj['left']//100}")
                elif obj["type"] == "path":
                    # Simple edge detection (for demo)
                    if len(obj["path"]) > 1:
                        start = obj["path"][0]
                        end = obj["path"][-1]
                        edges.append((
                            f"P{start[1]//100}",
                            f"R{end[1]//100}"
                        ))
            
            return edges
        return []

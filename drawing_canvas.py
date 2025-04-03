from streamlit_drawable_canvas import st_canvas
import streamlit as st
import numpy as np
class CanvasEditor:
    def __init__(self):
        self.canvas_width = 800
        self.canvas_height = 600
        self.node_size = 40
    def get_edges(self):
        """Simplified canvas with shape buttons"""
        st.markdown("### 🎨 Design Your System")
    # Add this visualization help
        st.markdown("""
        **Canvas Guide:**
        <div style="display: flex; gap: 20px; margin: 10px 0;">
            <div style="text-align: center">
                <img src="https://i.imgur.com/5XQJ3aE.png" width="150">
                <div>Processes (Rectangles)</div>
            </div>
            <div style="text-align: center">
                <img src="https://i.imgur.com/8K3zv9G.png" width="150">
                <div>Resources (Circles)</div>
            </div>
            <div style="text-align: center">
                <img src="https://i.imgur.com/3QZq1aT.png" width="150">
                <div>Connections (Lines)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Rest of canvas code
        st.image("deadlock.png", caption="Example: Draw processes as rectangles, resources as circles, connect with lines")
        # Shape selection buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            draw_process = st.button("Add Process (Rectangle)")
        with col2:
            draw_resource = st.button("Add Resource (Circle)")
        with col3:
            draw_line = st.button("Add Connection")
        
        # Set drawing mode
        drawing_mode = "rect" if draw_process else "circle" if draw_resource else "line"
        
        # Canvas example
       
        
        canvas_result = st_canvas(
            fill_color="rgba(255, 0, 0, 0.3)" if draw_process else "rgba(0, 255, 0, 0.3)",
            stroke_width=3,
            stroke_color="#000000",
            background_color="#FFFFFF",
            width=self.canvas_width,
            height=self.canvas_height,
            drawing_mode=drawing_mode,
            key="canvas"
        )
        
        if st.button("Analyze Drawing"):
            return self.parse_elements(canvas_result.json_data)
        return []

    def parse_elements(self, canvas_data):
        """Robust parsing without ID dependency"""
        nodes = []
        edges = []
        
        if canvas_data and "objects" in canvas_data:
            # First pass: Identify nodes
            for obj in canvas_data["objects"]:
                if obj["type"] == "rect":
                    nodes.append({
                        "type": "process",
                        "x": obj["left"] + obj["width"]/2,
                        "y": obj["top"] + obj["height"]/2,
                        "id": f"P{len(nodes)+1}"
                    })
                elif obj["type"] == "circle":
                    nodes.append({
                        "type": "resource",
                        "x": obj["left"],
                        "y": obj["top"],
                        "id": f"R{len(nodes)+1}"
                    })
            
            # Second pass: Identify connections
            for obj in canvas_data["objects"]:
                if obj["type"] == "line":
                    start = self.find_nearest_node(obj["x1"], obj["y1"], nodes)
                    end = self.find_nearest_node(obj["x2"], obj["y2"], nodes)
                    if start and end:
                        edges.append((start["id"], end["id"]))
        return edges

    def find_nearest_node(self, x, y, nodes):
        """Find nodes within 50px radius"""
        for node in nodes:
            dx = node["x"] - x
            dy = node["y"] - y
            if np.sqrt(dx**2 + dy**2) < 50:
                return node
        return None
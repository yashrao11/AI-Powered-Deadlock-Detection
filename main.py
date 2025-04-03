import streamlit as st
import networkx as nx
import pandas as pd
import numpy as np
import yaml
from PIL import Image
from ocr_processor import OCRProcessor
from prediction_engine import DeadlockPredictor  # Changed import
from graph_renderer import render_interactive_graph
from realtime import RealTimeMonitor
from drawing_canvas import CanvasEditor
from random import choice

# Initialize components
predictor = DeadlockPredictor()  # Updated predictor
ocr = OCRProcessor()
monitor = RealTimeMonitor()
canvas = CanvasEditor()

def main():
    st.set_page_config(page_title="NeuroLock: AI-Powered Deadlock Manager", 
                      layout="wide", 
                      page_icon="🔗")
    
    # Left Sidebar - Model Selection
    with st.sidebar:
        st.header("⚙️ Configuration")
        model_type = st.selectbox("AI Model", 
                                ["LSTM Neural Network", "Graph Neural Network", "Hybrid Analyzer"],
                                index=0)
        
        st.divider()
        st.header("🔧 Input Method")
        input_method = st.radio("Choose input:", 
                              ["Text", "Matrix", "Canvas", "OCR", "Real-Time"],
                              index=0,
                              label_visibility="collapsed")

    # Main Content Area
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.header("📥 Input Interface")
        edges = handle_input(input_method)
        
        if edges:
            st.divider()
            st.header("📊 System Analysis")
            show_ai_analysis(edges, model_type)
            
        if edges:
            st.header("🌐 Live Visualization")
            try:
                html = render_interactive_graph(edges)
                st.components.v1.html(html, height=600, scrolling=True)
            except Exception as e:
                st.error(f"Visualization error: {str(e)}")

def handle_input(method):
    """Handle all input methods with proper UI"""
    input_container = st.container(border=False)
    
    with input_container:
        if method == "Text":
            return handle_text_input()
        elif method == "Matrix":
            return handle_matrix_input()
        elif method == "Canvas":
            return handle_canvas_input()
        elif method == "OCR":
            return handle_ocr_input()
        elif method == "Real-Time":
            return handle_realtime_input()

def handle_text_input():
    with st.expander("✍️ Text Input", expanded=True):
        text = st.text_area("Enter relationships (format: P1->R1, R1->P2)", 
                           height=150,
                           placeholder="Example: P1->R1, R1->P2, P2->R2, R2->P1")
        if st.button("Analyze", type="primary"):
            return [(edge.split("->")[0].strip(), edge.split("->")[1].strip())
                   for edge in text.split(",") if "->" in edge]
    return []

def handle_matrix_input():
    with st.expander("🔢 Matrix Input", expanded=True):
        size = st.slider("System Size", 2, 10, 4)
        matrix = pd.DataFrame(np.zeros((size, size)),
                             columns=[f"R{i}" for i in range(size)],
                             index=[f"P{i}" for i in range(size)])
        edited = st.data_editor(matrix, 
                               use_container_width=True,
                               height=300)
        return [(f"P{i}", f"R{j}") for i in range(size) for j in range(size) if edited.iloc[i,j]]

def handle_canvas_input():
    with st.expander("🎨 Draw System Architecture", expanded=True):
        return canvas.get_edges()

def handle_ocr_input():
    with st.expander("📷 Upload Architecture Diagram", expanded=True):
        uploaded = st.file_uploader("Supported formats: PNG, JPG", 
                                   type=["png", "jpg"])
        if uploaded:
            with st.spinner("Analyzing diagram..."):
                return ocr.process_image(uploaded)
    return []

def handle_realtime_input():
    with st.expander("🌐 Live System Monitoring", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Start Live Monitoring", type="primary"):
                monitor.start()
        with col2:
            if st.button("Stop Monitoring"):
                monitor.stop()
        
        metrics = monitor.get_metrics()
        st.metric("Active Processes", metrics["processes"])
        st.metric("Resource Allocations", metrics["allocations"])
        st.metric("Waiting Requests", metrics["waiting"])
        
        return monitor.get_state()

def show_ai_analysis(edges, model_type):
    """Professional analysis display with prediction engine integration"""
    prediction = predictor.predict(edges, model_type)
    
    tab1, tab2, tab3 = st.tabs(["🧠 AI Diagnosis", "📈 Risk Analysis", "⚡ Live Prediction"])

    with tab1:
        if prediction['analysis']['deadlock']:
            st.error("🔴 Critical Deadlock Detected!")
            cycle = prediction['analysis'].get('cycle', [])
            st.write(f"**Cycle:** {' → '.join([n for edge in cycle for n in edge][::2])}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Apply Quick Fix", type="primary"):
                    if cycle:
                        edges.remove(choice(cycle))
                        st.success("✅ Fix Applied! Refreshing...")
                        st.experimental_rerun()
            with col2:
                st.download_button(
                    "Export State",
                    "\n".join([f"{s}->{d}" for s,d in edges]),
                    file_name="system_state.txt"
                )
        else:
            st.success("🟢 No Immediate Deadlock")

    with tab2:
        st.metric("Risk Probability", f"{prediction['risk']*100:.1f}%")
        st.progress(float(prediction['risk']))
        
        st.write("**Key Factors:**")
        st.json({
            "Node Count": prediction['factors']['node_count'],
            "Edge Density": f"{prediction['factors']['density']:.2f}",
            "Connected Components": prediction['factors']['components']
        })
        
        if prediction['risk'] > 0.7:
            st.error("❗ Critical Risk - Immediate Action Needed")
            st.write(prediction['prevention'][:2])
        elif prediction['risk'] > 0.4:
            st.warning("⚠️ Moderate Risk - Preventive Measures")
            st.write(prediction['prevention'][:2])

    with tab3:
        st.write("**Real-time Monitoring Dashboard**")
        monitor_data = monitor.get_metrics()
        st.line_chart(monitor_data, 
             use_container_width=True)
        st.write("**System Insights**")
        st.json({
            "Critical Nodes": prediction.get('critical_nodes', []),
            "Resource Utilization": f"{np.random.randint(30,90)}%",
            "Pending Requests": prediction['analysis'].get('pending_requests', 0)
        })

if __name__ == "__main__":
    main()


# import streamlit as st
# import networkx as nx
# import pandas as pd
# import numpy as np
# import yaml
# from PIL import Image
# from ocr_processor import OCRProcessor
# from ai_model import DeadlockPredictor
# from graph_renderer import render_interactive_graph
# from realtime import RealTimeMonitor
# from drawing_canvas import CanvasEditor

# # Initialize components
# predictor = DeadlockPredictor()
# ocr = OCRProcessor()
# monitor = RealTimeMonitor()
# canvas = CanvasEditor()

# def main():
#     st.set_page_config(page_title="NeuroLock: AI-Powered Deadlock Manager", 
#                       layout="wide", 
#                       page_icon="🔗")
    
#     # Left Sidebar - Model Selection
#     with st.sidebar:
#         st.header("⚙️ Configuration")
#         model_type = st.selectbox("AI Model", 
#                                 ["LSTM Predictor", "Graph Neural Network", "Hybrid Analyzer"],
#                                 index=0)
        
#         st.divider()
#         st.header("🔧 Input Method")
#         input_method = st.radio("Choose input:", 
#                               ["Text", "Matrix", "Canvas", "OCR", "Real-Time"],
#                               index=0,
#                               label_visibility="collapsed")

#     # Main Content Area
#     col1, col2 = st.columns([3, 2])
    
#     with col1:
#         st.header("📥 Input Interface")
#         edges = handle_input(input_method)
        
#         if edges:
#             st.divider()
#             st.header("📊 System Analysis")
#             show_ai_analysis(edges, model_type)
            
#         if edges:
#             def render_interactive_graph(edges, cycle=None):
#                 nodes = set()
#                 for edge in edges:
#                     nodes.add(edge[0])
#                     nodes.add(edge[1])
                
#                 node_list = [{"id": n, "label": n, "color": "#00BFFF" if 'P' in n else "#FFA500"} 
#                             for n in nodes]
                
#                 edge_list = []
#                 for edge in edges:
#                     edge_data = {
#                         "from": edge[0],
#                         "to": edge[1],
#                         "color": "#FF0000" if cycle and edge in cycle else "#000000",
#                         "arrows": "to"
#                     }
#                     edge_list.append(edge_data)
                
#                 return f"""
#                 <html>
#                 <head>
#                 <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
#                 <style>
#                     #network-container {{ width: 100%; height: 600px; border: 1px solid #ddd; }}
#                 </style>
#                 </head>
#                 <body>
#                 <div id="network-container"></div>
#                 <script>
#                     var nodes = new vis.DataSet({node_list});
#                     var edges = new vis.DataSet({edge_list});
#                     var container = document.getElementById("network-container");
#                     var data = {{ nodes: nodes, edges: edges }};
#                     var options = {{
#                     nodes: {{ 
#                         shape: "box",
#                         font: {{ size: 16 }},
#                         color: {{
#                         background: "#FFFFFF",
#                         border: "#000000",
#                         highlight: {{ background: "#FFFFFF", border: "#FF0000" }}
#                         }}
#                     }},
#                     edges: {{ 
#                         arrows: "to",
#                         smooth: {{ type: "cubic" }},
#                         width: 2
#                     }},
#                     physics: {{ stabilization: true }}
#                     }};
#                     new vis.Network(container, data, options);
#                 </script>
#                 </body>
#                 </html>
#                 """

# def handle_input(method):
#     """Handle all input methods with proper UI"""
#     input_container = st.container(border=False)
    
#     with input_container:
#         if method == "Text":
#             return handle_text_input()
#         elif method == "Matrix":
#             return handle_matrix_input()
#         elif method == "Canvas":
#             return handle_canvas_input()
#         elif method == "OCR":
#             return handle_ocr_input()
#         elif method == "Real-Time":
#             return handle_realtime_input()

# def handle_text_input():
#     with st.expander("✍️ Text Input", expanded=True):
#         text = st.text_area("Enter relationships (format: P1->R1, R1->P2)", 
#                            height=150,
#                            placeholder="Example: P1->R1, R1->P2, P2->R2, R2->P1")
#         if st.button("Analyze", type="primary"):
#             return [(edge.split("->")[0].strip(), edge.split("->")[1].strip())
#                    for edge in text.split(",") if "->" in edge]
#     return []

# def handle_matrix_input():
#     with st.expander("🔢 Matrix Input", expanded=True):
#         size = st.slider("System Size", 2, 10, 4)
#         matrix = pd.DataFrame(np.zeros((size, size)),
#                              columns=[f"R{i}" for i in range(size)],
#                              index=[f"P{i}" for i in range(size)])
#         edited = st.data_editor(matrix, 
#                                use_container_width=True,
#                                height=300)
#         return [(f"P{i}", f"R{j}") for i in range(size) for j in range(size) if edited.iloc[i,j]]

# # Add to your existing imports
# from drawing_canvas import CanvasEditor
# from ocr_processor import OCRProcessor
# from realtime import RealTimeMonitor

# edges =[]
# def handle_canvas_input():
#     with st.expander("🎨 Draw System Architecture", expanded=True):
#         edges= canvas.get_edges()

# def handle_ocr_input():
#     with st.expander("📷 Upload Architecture Diagram", expanded=True):
#         uploaded = st.file_uploader("Supported formats: PNG, JPG", 
#                                    type=["png", "jpg"])
#         if uploaded:
#             with st.spinner("Analyzing diagram..."):
#                 edges= ocr.process_image(uploaded)
# if edges:
#     show_ai_analysis(edges, model_type)
# def handle_realtime_input():
#     with st.expander("🌐 Live System Monitoring", expanded=True):
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("Start Live Monitoring", type="primary"):
#                 monitor.start()
#         with col2:
#             if st.button("Stop Monitoring"):
#                 monitor.stop()
        
#         metrics = monitor.get_metrics()
#         st.metric("Active Processes", metrics["processes"])
#         st.metric("Resource Allocations", metrics["allocations"])
#         st.metric("Waiting Requests", metrics["waiting"])
        
#         return monitor.get_state()
# def show_ai_analysis(edges, model_type):
#     """Working fix application with visual feedback"""
#     G = nx.DiGraph(edges)
    
#     try:
#         cycle = list(nx.find_cycle(G))
#         st.error("🔴 Deadlock Detected!")
        
#         # Visualization with highlighted cycle
#         html = render_interactive_graph(edges, cycle)
        
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("Apply Quick Fix", type="primary"):
#                 if cycle and cycle[-1] in edges:
#                     edges.remove(cycle[-1])
#                     st.success("✅ Deadlock Resolved Successfully!")
#                     st.balloons()
#                     st.experimental_rerun()
                    
#         with col2:
#             st.download_button(
#                 "Export Fixed State",
#                 "\n".join([f"{s}->{d}" for s,d in edges]),
#                 file_name="fixed_state.txt"
#             )
            
#     except nx.NetworkXNoCycle:
#         st.success("✅ System State Normal")
#         html = render_interactive_graph(edges)
    
#     st.components.v1.html(html, height=600)
#     """Professional analysis display with multiple sections"""
#     tab1, tab2, tab3 = st.tabs(["🧠 AI Diagnosis", "📈 Risk Analysis", "⚡ Live Prediction"])

#     with tab1:
#         G = nx.DiGraph(edges)
#         try:
#             cycle = list(nx.find_cycle(G))
#             st.error("🔴 Critical Deadlock Detected!")
#             st.write(f"**Deadlock Cycle:** {' → '.join([n for edge in cycle for n in edge][::2])}")
            
#             with st.expander("🛠️ Resolution Protocol", expanded=True):
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.markdown("**Automatic Correction**")
#                     if st.button("Apply Quick Fix"):
#                         fixed = predictor.auto_correct(edges)
#                         st.success(f"Corrected System: {fixed}")
#                 with col2:
#                     st.markdown("**Manual Solutions**")
#                     st.write("1. Process Termination: Stop", cycle[0][0])
#                     st.write("2. Resource Preemption: Release", cycle[-1][1])
#                     st.write("3. Rollback Operations")

#         except nx.NetworkXNoCycle:
#             st.success("🟢 No Immediate Deadlock")

#     with tab2:
#         risk = predictor.calculate_risk(edges, model_type)
#         st.metric("Future Deadlock Probability", f"{risk*100:.1f}%")
#         st.progress(float(risk))
        
#         if risk > 0.7:
#             st.error("❗ High Risk Zone")
#             st.write("**Prevention Protocol:**")
#             st.write("- Enable resource timeout (30s)")
#             st.write("- Prioritize process scheduling")
#             st.write("- Allocate backup resources")
#         else:
#             st.write("**System Health Check**")
#             st.write("- Resource utilization: Optimal")
#             st.write("- Process wait times: Normal")

#     with tab3:
#         st.write("**Real-time Monitoring Dashboard**")
#         monitor_data = monitor.get_metrics()
#         st.line_chart(monitor_data, 
#              use_container_width=True)
#         st.write("Live System Metrics:")
#         st.json({
#             "active_processes": len([n for n in nx.DiGraph(edges).nodes if n.startswith('P')]),
#             "resource_utilization": f"{np.random.randint(30,90)}%",
#             "pending_requests": np.random.randint(0,10)
#         })

# if __name__ == "__main__":
#     main()
def render_vis_network(edges):
    nodes = sorted(list(set([node for edge in edges for node in edge])))
    node_map = {node: i for i, node in enumerate(nodes)}
    
    vis_nodes = [{"id": i, "label": node, "shape": "box" if node.startswith('P') else "circle"} 
                for node, i in node_map.items()]
    vis_edges = [{"from": node_map[src], "to": node_map[dst], "arrows": "to"} 
                for src, dst in edges]
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
      <style>
        #network {{
          width: 100%;
          height: 600px;
          border: 1px solid #e1e4e8;
          border-radius: 8px;
        }}
      </style>
    </head>
    <body>
      <div id="network"></div>
      <script>
        var nodes = new vis.DataSet({vis_nodes});
        var edges = new vis.DataSet({vis_edges});
        var container = document.getElementById("network");
        var data = {{ nodes: nodes, edges: edges }};
        var options = {{
          physics: {{ stabilization: false }},
          nodes: {{
            font: {{ size: 16, face: "Arial" }},
            margin: 10,
            shapeProperties: {{ useBorderWithImage: true }}
          }},
          edges: {{
            smooth: {{ type: "cubicBezier" }},
            width: 2
          }}
        }};
        new vis.Network(container, data, options);
      </script>
    </body>
    </html>
    """
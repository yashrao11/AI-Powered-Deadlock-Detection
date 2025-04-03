def render_interactive_graph(edges, cycle=None):
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    
    node_list = [{"id": n, "label": n, "color": "#00BFFF" if 'P' in n else "#FFA500"} 
                for n in nodes]
    
    edge_list = []
    for edge in edges:
        edge_data = {
            "from": edge[0],
            "to": edge[1],
            "color": "#FF0000" if cycle and edge in cycle else "#000000",
            "arrows": "to"
        }
        edge_list.append(edge_data)
    
    return f"""
    <html>
    <head>
      <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
      <style>
        #network-container {{ width: 100%; height: 600px; border: 1px solid #ddd; }}
      </style>
    </head>
    <body>
      <div id="network-container"></div>
      <script>
        var nodes = new vis.DataSet({node_list});
        var edges = new vis.DataSet({edge_list});
        var container = document.getElementById("network-container");
        var data = {{ nodes: nodes, edges: edges }};
        var options = {{
          nodes: {{ 
            shape: "box",
            font: {{ size: 16 }},
            color: {{
              background: "#FFFFFF",
              border: "#000000",
              highlight: {{ background: "#FFFFFF", border: "#FF0000" }}
            }}
          }},
          edges: {{ 
            arrows: "to",
            smooth: {{ type: "cubic" }},
            width: 2
          }},
          physics: {{ stabilization: true }}
        }};
        new vis.Network(container, data, options);
      </script>
    </body>
    </html>
    """
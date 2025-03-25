"# AI Deadlock Detection Code" 
import networkx as nx
import matplotlib.pyplot as plt

def detect_deadlock(processes, resources, allocations):
    G = nx.DiGraph()

    # Add process and resource nodes
    for p in processes:
        G.add_node(p, color="blue")
    for r in resources:
        G.add_node(r, color="red")

    # Add allocation edges
    for p, r in allocations:
        G.add_edge(p, r)

    # Check for cycles (deadlocks)
    try:
        cycle = nx.find_cycle(G, orientation="original")
        print("Deadlock detected! Cycle:", cycle)
    except nx.NetworkXNoCycle:
        print("No deadlock detected.")

    # Draw the graph
    colors = ["blue" if node in processes else "red" for node in G.nodes()]
    nx.draw(G, with_labels=True, node_color=colors)
    plt.show()

if __name__ == "__main__":
    processes = ["P1", "P2", "P3"]
    resources = ["R1", "R2"]
    allocations = [("P1", "R1"), ("P2", "R2"), ("R1", "P2"), ("R2", "P3")]

    detect_deadlock(processes, resources, allocations)

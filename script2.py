from src.deadlock import detect_deadlock
from src.visualization import visualize_rag
import networkx as nx

# Step 1: Create a Resource Allocation Graph (RAG)
G = nx.DiGraph()
G.add_edges_from([
    ("P1", "R1"),  # Process P1 holds Resource R1
    ("R1", "P2"),  # Resource R1 is requested by Process P2
    ("P2", "R2"),  # Process P2 holds Resource R2
    ("R2", "P3"),  # Resource R2 is requested by Process P3
    ("P3", "R1")   # Deadlock: Process P3 waits for Resource R1, forming a cycle
])

# Step 2: Detect Deadlock
deadlock_cycle = detect_deadlock(G)

# Step 3: Print and Visualize the Graph
if deadlock_cycle:
    print("🔴 Deadlock detected! Cycle:", deadlock_cycle)
else:
    print("✅ No deadlock detected.")

visualize_rag(G, deadlock_cycle)

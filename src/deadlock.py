import networkx as nx

def detect_deadlock(graph):
    """Detects deadlock by checking for cycles in the Resource Allocation Graph."""
    try:
        cycle = nx.find_cycle(graph, orientation="original")  # Detects cycles
        return cycle  # Deadlock found
    except nx.NetworkXNoCycle:
        return None  # No deadlock

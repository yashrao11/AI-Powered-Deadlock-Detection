import networkx as nx

def detect_deadlock(edges):
    graph = nx.DiGraph()  # Ensure it's a directed graph

    for edge in edges:
        u, v = edge
        if u == v:
            return True, [[u, v]]  # Self-loop is a deadlock

        graph.add_edge(u, v)

    try:
        cycle = nx.find_cycle(graph, orientation="original")
        return True, cycle  # Deadlock detected
    except nx.NetworkXNoCycle:
        return False, []  # No deadlock

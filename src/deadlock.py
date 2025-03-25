import networkx as nx

def detect_deadlock(graph):
    """
    Detects a cycle in the given directed graph.
    If a cycle is found, it indicates a deadlock.
    
    :param graph: NetworkX directed graph (DiGraph)
    :return: List representing the deadlock cycle, or None if no deadlock
    """
    try:
        cycle = nx.find_cycle(graph, orientation="original")
        return [node for node, _, _ in cycle]  # Extract only node names from cycle
    except nx.NetworkXNoCycle:
        return None  # No deadlock detected

def suggest_deadlock_solution(graph, cycle):
    """
    Suggests a possible fix for resolving the detected deadlock.
    
    :param graph: NetworkX directed graph (DiGraph)
    :param cycle: List of nodes forming the deadlock cycle
    :return: String message suggesting a possible fix
    """
    if not cycle:
        return "No deadlock detected."

    # Strategy: Suggest releasing one of the locked resources in the cycle
    for node in cycle:
        if "R" in node:  # Identify resources in the cycle
            return f"🔄 Consider releasing Resource '{node}' to break the deadlock."

    return "❗ Deadlock detected, but no immediate resolution found. Consider terminating a process."


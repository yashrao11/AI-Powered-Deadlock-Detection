import networkx as nx

def detect_deadlock(edges):
    """
    Detects all deadlock cycles in the given resource allocation graph.
    
    :param edges: List of tuples representing process-resource relationships.
    :return: Tuple (deadlock_detected, cycles) where:
             - deadlock_detected (bool): True if any cycle is found.
             - cycles (list): A list of cycles detected in the graph.
    """
    graph = nx.DiGraph()  # Create a directed graph

    for edge in edges:
        u, v = edge
        # Handle self-loops as an immediate deadlock
        if u == v:
            return True, [[u, v]]
        graph.add_edge(u, v)

    # Get all cycles in the graph using simple_cycles
    cycles = list(nx.simple_cycles(graph))
    if cycles:
        return True, cycles  # Deadlock detected with all cycles
    else:
        return False, []  # No deadlock detected

def suggest_deadlock_solution(cycles):
    """
    Provides suggestions to resolve detected deadlock cycles.
    
    :param cycles: List of cycles (each cycle is a list of nodes).
    :return: A string with suggestions for each detected cycle.
    """
    suggestions = []
    for cycle in cycles:
        # Example suggestion: terminate the first process in the cycle
        suggestions.append(f"Consider terminating process '{cycle[0]}' to break the cycle: {cycle}")
    return "\n".join(suggestions)

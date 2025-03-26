import networkx as nx

def detect_all_deadlocks(edges):
    """
    Detects all deadlocks (cycles) in the given process-resource graph.

    :param edges: List of tuples representing process-resource relationships.
    :return: List of detected cycles (deadlocks).
    """
    graph = nx.DiGraph()  # Directed graph for process-resource allocation
    graph.add_edges_from(edges)

    deadlocks = []
    
    try:
        # Find all cycles in the graph
        cycles = list(nx.simple_cycles(graph))
        deadlocks.extend(cycles)
    except nx.NetworkXNoCycle:
        pass  # No cycles found, so no deadlocks

    return deadlocks

def suggest_deadlock_solution(cycles):
    """
    Suggests solutions for detected deadlocks.

    :param cycles: List of cycles detected in the graph.
    :return: List of suggested solutions.
    """
    solutions = []
    for cycle in cycles:
        process = cycle[0]  # Get first process in cycle
        solutions.append(f"Terminate process {process} to break deadlock.")

    return solutions if solutions else ["No deadlock resolution needed."]

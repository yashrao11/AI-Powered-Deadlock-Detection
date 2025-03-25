import networkx as nx

def detect_deadlock(edges):
    """
    Detects deadlocks in a resource allocation graph.

    :param edges: List of tuples representing process-resource relationships.
    :return: Tuple (deadlock_detected, cycles) where:
             - deadlock_detected (bool): True if a cycle (deadlock) is found.
             - cycles (list): List of cycles detected in the graph.
    """
    graph = nx.DiGraph()  # Create a directed graph
    graph.add_edges_from(edges)  # Add edges from the input list

    try:
        cycle = nx.find_cycle(graph, orientation="original")  # Detect cycles
        return True, cycle  # Deadlock detected
    except nx.NetworkXNoCycle:
        return False, []  # No deadlock

def suggest_deadlock_solution(cycles):
    """
    Suggests solutions for detected deadlocks.

    :param cycles: List of cycles detected in the graph.
    :return: List of suggested solutions.
    """
    solutions = []
    for cycle in cycles:
        process, resource = cycle[0]  # Get first process-resource in cycle
        solutions.append(f"Terminate process {process} to break deadlock.")

    return solutions if solutions else ["No deadlock resolution needed."]

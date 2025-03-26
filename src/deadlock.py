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

import networkx as nx

def detect_all_deadlocks(edges):
    """
    Detects deadlocks using a DFS-based cycle detection for faster execution.
    :param edges: List of tuples representing process-resource relationships.
    :return: List of detected cycles (deadlocks).
    """
    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    def find_cycles(node, visited, stack):
        """DFS-based cycle detection."""
        if node in stack:  # Cycle detected
            return [stack[stack.index(node):]]
        
        if node in visited:
            return []
        
        visited.add(node)
        stack.append(node)
        cycles = []
        for neighbor in graph.neighbors(node):
            cycles.extend(find_cycles(neighbor, visited, stack))
        
        stack.pop()
        return cycles

    all_cycles = []
    visited_nodes = set()

    for node in graph.nodes():
        if node not in visited_nodes:
            cycles = find_cycles(node, visited_nodes, [])
            all_cycles.extend(cycles)

    return all_cycles  # Returns list of cycles (deadlocks)

def suggest_deadlock_solution(cycles):
    """Suggests a solution to break deadlocks."""
    solutions = []
    for cycle in cycles:
        process = cycle[0]  
        solutions.append(f"Terminate process {process} to break deadlock.")

    return solutions if solutions else ["No deadlock resolution needed."]

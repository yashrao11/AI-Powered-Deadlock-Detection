def suggest_deadlock_solution(deadlock_cycle):
    if deadlock_cycle:
        return f"Consider terminating {deadlock_cycle[0]} or manually releasing {deadlock_cycle[-1]}"
    return "No action needed."

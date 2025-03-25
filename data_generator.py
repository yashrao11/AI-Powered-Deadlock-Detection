import networkx as nx
import random
import pandas as pd

def generate_synthetic_data(samples=1000):
    data = []
    
    for _ in range(samples):
        G = nx.DiGraph()
        num_processes = random.randint(2, 6)
        num_resources = random.randint(2, 6)
        
        processes = [f'P{i}' for i in range(1, num_processes + 1)]
        resources = [f'R{i}' for i in range(1, num_resources + 1)]
        
        # Randomly create edges between processes and resources
        for _ in range(random.randint(3, 10)):
            p = random.choice(processes)
            r = random.choice(resources)
            if random.random() < 0.5:
                G.add_edge(p, r)  # Process requests resource
            else:
                G.add_edge(r, p)  # Resource assigned to process
                
        # Check if there's a deadlock
        deadlock = 1 if any(nx.simple_cycles(G)) else 0
        data.append((G.edges, deadlock))
    
    # Convert to DataFrame for easy handling
    df = pd.DataFrame(data, columns=['Graph', 'Deadlock'])
    return df

# Generate data and save
if __name__ == "__main__":
    df = generate_synthetic_data(1000)
    df.to_csv("deadlock_dataset.csv", index=False)
    print("✅ Synthetic dataset created: deadlock_dataset.csv")

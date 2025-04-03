import threading
import time
import random
import numpy as np

class RealTimeMonitor:
    def __init__(self):
        self.running = False
        self.edges = []
        self.lock = threading.Lock()
        self.processes = ["P1", "P2", "P3"]
        self.resources = ["R1", "R2", "R3"]
        
    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.simulate)
            self.thread.start()
            
    def stop(self):
        self.running = False
        
    def simulate(self):
        """Generate realistic allocation patterns"""
        while self.running:
            with self.lock:
                # Clear old allocations
                self.edges.clear()
                
                # Create plausible allocations
                for p in self.processes:
                    if random.random() > 0.4:
                        resource = random.choice(self.resources)
                        self.edges.append((p, resource))
                        if random.random() > 0.6:  # Simulate resource holding
                            self.edges.append((resource, random.choice(self.processes)))
                
                time.sleep(2)  # Update every 2 seconds
    
    def get_state(self):
        with self.lock:
            return self.edges.copy()
    
    def get_metrics(self):
        return {
            "processes": len(self.processes),
            "resources": len(self.resources),
            "allocations": len(self.edges),
            "waiting": np.random.randint(0, 5)
        }
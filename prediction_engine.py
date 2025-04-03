import networkx as nx
import numpy as np

class DeadlockPredictor:
    def predict(self, edges, model_type="Hybrid", sensitivity=1.0):
        """Enhanced prediction with model differentiation"""
        G = nx.DiGraph(edges)
        
        base_factors = {
            'node_count': len(G.nodes()),
            'edge_count': len(G.edges()),
            'density': nx.density(G),
            'components': nx.number_strongly_connected_components(G),
            'avg_degree': np.mean([d for _, d in G.degree()])
        }
        
        if model_type == "LSTM Neural Network":
            risk = self._lstm_prediction(base_factors, sensitivity)
        elif model_type == "Graph Neural Network":
            risk = self._gnn_prediction(G, sensitivity)
        else:  # Hybrid
            risk = self._hybrid_prediction(G, base_factors, sensitivity)
            
        return {
            "risk": risk,
            "factors": base_factors,
            "analysis": self._deadlock_analysis(G),
            "prevention": self._get_prevention(risk)
        }

    def _lstm_prediction(self, factors, sensitivity):
        """Temporal pattern simulation"""
        return min(0.99, 
            (factors['edge_count']/20 + 
             factors['components']/5) * 
            sensitivity * 1.2
        )

    def _gnn_prediction(self, G, sensitivity):
        """Graph structure analysis"""
        try:
            cycle_length = len(next(nx.simple_cycles(G)))
        except StopIteration:
            cycle_length = 0
        return min(0.99, 
            (cycle_length/10 * sensitivity * 1.5)
        )

    def _hybrid_prediction(self, G, factors, sensitivity):
        """Combined approach"""
        lstm = self._lstm_prediction(factors, 1)
        gnn = self._gnn_prediction(G, 1)
        return min(0.99, ((lstm + gnn)/2 * sensitivity))

    def _deadlock_analysis(self, G):
        """Detailed cycle analysis"""
        try:
            cycle = list(nx.find_cycle(G))
            return {
                "deadlock": True,
                "cycle_nodes": list(set([n for edge in cycle for n in edge])),
                "cycle_length": len(cycle),
                "criticality": "High" if len(cycle) < 5 else "Medium"
            }
        except nx.NetworkXNoCycle:
            return {"deadlock": False}

    def _get_prevention(self, risk):
        """Prevention strategies based on risk"""
        if risk > 0.8:
            return ["Force terminate oldest process", "Preempt critical resource"]
        elif risk > 0.5:
            return ["Rollback allocations", "Add timeout mechanisms"]
        return ["Monitor system", "Optimize scheduling"]
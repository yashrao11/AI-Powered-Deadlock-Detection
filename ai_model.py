import tensorflow as tf
import networkx as nx
import numpy as np
import yaml
from sklearn.preprocessing import StandardScaler

class DeadlockPredictor:
    def __init__(self):
        with open("config.yaml") as f:
            self.config = yaml.safe_load(f).get('ai', {})
            
        self.model = self.build_model()
        self.scaler = StandardScaler()
        self.risk_history = []
        
    def build_model(self):
        """Build and compile the neural network model"""
        model = tf.keras.Sequential([
            tf.keras.layers.LSTM(128, 
                               input_shape=(self.config.get('sequence_length', 20), 
                               self.config.get('num_features', 5))),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', 
                     loss='binary_crossentropy',
                     metrics=['accuracy'])
        return model
    
    def calculate_risk(self, edges, model_type="LSTM Predictor"):
        """Calculate deadlock risk probability with proper input shaping"""
        G = nx.DiGraph(edges)
        
        if model_type == "LSTM Predictor":
            # Create sequence data with padding
            features = self.create_sequence_input(G)
            risk = self.model.predict(features)[0][0]
        else:
            risk = self.graph_based_risk(G)
            
        self.risk_history.append(risk)
        return risk
    
    def create_sequence_input(self, G):
        """Create sequence input for LSTM with padding"""
        seq_length = self.config.get('sequence_length', 20)
        num_features = self.config.get('num_features', 5)
        
        # Get current features
        current_features = self.extract_lstm_features(G)
        
        # Create sequence by repeating current features
        sequence = np.array([current_features] * seq_length)
        
        # Reshape to (1, seq_length, num_features)
        return sequence.reshape(1, seq_length, num_features)
    
    def extract_lstm_features(self, G):
        """Feature extraction for LSTM model"""
        features = np.zeros(5)
        features[0] = len(G.edges()) / 10  # Normalized edge count
        features[1] = nx.density(G)        # Graph density
        features[2] = len(G.nodes()) / 10  # Normalized node count
        features[3] = nx.number_strongly_connected_components(G) / 5
        features[4] = len(list(nx.simple_cycles(G))) / 5
        return self.scaler.fit_transform([features])[0]
    
    def graph_based_risk(self, G):
        """Alternative risk calculation for graph-based models"""
        try:
            cycle = nx.find_cycle(G)
            return 0.9  # High risk if cycle exists
        except nx.NetworkXNoCycle:
            return min(0.8, len(G.edges()) / 20)  # Scale risk with edge count
    
    def auto_correct(self, edges):
        """Automatically correct deadlock by breaking cycle"""
        G = nx.DiGraph(edges)
        try:
            cycle = list(nx.find_cycle(G))
            st.success("✅ System State Normal")
            # Remove the last edge in the cycle
            return [edge for edge in edges if edge != cycle[-1]]
        except nx.NetworkXNoCycle:
            return edges
    
    def get_risk_history(self):
        """Return risk history for visualization"""
        return self.risk_history[-20:]
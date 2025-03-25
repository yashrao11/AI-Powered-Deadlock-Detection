import joblib
import pandas as pd
import ast

# Load the trained model
model = joblib.load("deadlock_model.pkl")

# Function to predict deadlock
def predict_deadlock(graph_edges):
    # Convert the input graph to the same feature format
    edge_count = len(graph_edges)
    
    # Create a DataFrame with the correct feature name
    input_data = pd.DataFrame({"edge_count": [edge_count]})  # FIXED: Matched feature name exactly

    # Predict using the trained model
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        print("🔴 Deadlock detected!")
    else:
        print("✅ No deadlock detected.")

# Example: Testing the model with a new graph
test_graph = "[('P1', 'R1'), ('R1', 'P2'), ('P2', 'R2'), ('R2', 'P3'), ('P3', 'R1')]"  # Deadlock example
graph_edges = ast.literal_eval(test_graph)
predict_deadlock(graph_edges)

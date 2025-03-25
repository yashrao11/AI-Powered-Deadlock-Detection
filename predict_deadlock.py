import joblib
import pandas as pd
import ast
import networkx as nx
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load("deadlock_model.pkl")

# Function to visualize the RAG
def visualize_rag(graph_edges, deadlock_detected):
    G = nx.DiGraph()
    G.add_edges_from(graph_edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10)

    if deadlock_detected:
        plt.title("🔴 Deadlock Detected")
    else:
        plt.title("✅ No Deadlock Detected")

    plt.show()

# Function to predict and visualize deadlocks
def predict_and_visualize(graph_edges):
    # Convert the input graph to the same feature format
    edge_count = len(graph_edges)
    input_data = pd.DataFrame({"edge_count": [edge_count]})  # Ensure feature name matches training data

    # Predict deadlock
    prediction = model.predict(input_data)[0]

    # Print result
    if prediction == 1:
        print("🔴 Deadlock detected!")
    else:
        print("✅ No deadlock detected.")

    # Visualize the graph
    visualize_rag(graph_edges, prediction == 1)

# Example: Testing the model with a new graph
test_graph = "[('P1', 'R1'), ('R1', 'P2'), ('P2', 'R2'), ('R2', 'P3'), ('P3', 'R1')]"  # Deadlock example
graph_edges = ast.literal_eval(test_graph)
predict_and_visualize(graph_edges)
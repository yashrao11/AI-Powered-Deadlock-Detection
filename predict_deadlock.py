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

# Function to run multiple test cases
def run_tests():
    test_cases = {
        "Deadlock Case": "[('P1', 'R1'), ('R1', 'P2'), ('P2', 'R2'), ('R2', 'P3'), ('P3', 'R1')]",
        "No Deadlock Case": "[('P1', 'R1'), ('R1', 'P2'), ('P2', 'R2')]"
    }

    for name, test_graph in test_cases.items():
        print(f"\n🔹 Running test: {name}")
        graph_edges = ast.literal_eval(test_graph)
        predict_and_visualize(graph_edges)

# Main function for user input
def main():
    print("\n🔹 AI-Powered Deadlock Detection System 🔹")
    choice = input("Do you want to enter a custom graph? (yes/no): ").strip().lower()

    if choice == "yes":
        user_graph = input("Enter the graph as a list of edges (e.g., [('P1', 'R1'), ('R1', 'P2')]): ")
        try:
            graph_edges = ast.literal_eval(user_graph)
            predict_and_visualize(graph_edges)
        except (SyntaxError, ValueError):
            print("❌ Invalid input format. Please enter a valid list of tuples.")
    else:
        print("\n🔹 Running predefined test cases...")
        run_tests()

# Run the program
if __name__ == "__main__":
    main()

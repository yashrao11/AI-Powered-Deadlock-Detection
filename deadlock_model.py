import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import ast  # To convert string representation of a list to an actual list

# Load dataset
df = pd.read_csv("/content/deadlock_dataset.csv")

# Convert string representation of Graph (list of edges) into numerical feature
def process_graph(graph_str):
    try:
        graph_edges = ast.literal_eval(graph_str)  # Convert string to list
        return len(graph_edges)  # Feature: Number of edges in the graph
    except:
        return 0  # In case of an invalid format

df["edge_count"] = df["Graph"].apply(process_graph)  # Convert 'Graph' column

# Prepare features and target
X = df[["edge_count"]]  # Features
y = df["Deadlock"]  # Target (1 = Deadlock, 0 = No Deadlock)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Training Complete! Accuracy: {accuracy:.2f}")

# Save trained model
joblib.dump(model, "deadlock_model.pkl")
print("💾 Model saved as 'deadlock_model.pkl'")

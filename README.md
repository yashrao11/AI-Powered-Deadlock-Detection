# 🚀 AI-Powered Deadlock Detection System

A real-time intelligent system designed to **detect, predict, and resolve deadlocks** using **Machine Learning**, **Graph Neural Networks**, **LSTM**, and **Graph Theory**. Built for operating systems, process simulation, and academic research, this tool analyzes resource allocation graphs and proactively mitigates deadlock risks.

---

## 🌐 Live Demo

🔗 [Click here to try the deployed Streamlit app](https://requirementstxt-dzzjgv5ijvpcpzskiae8bg.streamlit.app/)

---

## 📌 Key Features

✅ **Deadlock Detection**: Analyzes resource allocation graphs and identifies cycles representing deadlocks using DFS-based algorithms.  
✅ **Deadlock Prediction (AI)**: Uses hybrid AI models (GNN + LSTM) to predict if a deadlock is likely to occur in the near future.  
✅ **Multi-Input Support**: Accepts graphs through:
- Manual entry (text format)
- Matrix format
- Sketch-based drawing
- OCR from screenshots

✅ **Graph Visualization**: Live visualization using `NetworkX` and `vis-network` to highlight nodes and edges involved in deadlocks.  
✅ **Real-Time Dashboard**: Built with Streamlit to monitor ongoing system states and show dynamic prediction graphs.  
✅ **Automatic Resolution Suggestions**: Offers automated recommendations to release/kill processes to resolve deadlocks.

---

## 🧠 Technologies & Concepts Used

### 👨‍💻 Programming & Libraries
- **Python 3.10**
- `NetworkX` – For graph creation and cycle detection
- `Streamlit` – For real-time dashboard and deployment
- `OpenCV + Tesseract OCR` – For image-to-graph recognition
- `TensorFlow / Keras` – For LSTM model
- `PyTorch Geometric` – For Graph Neural Networks (GNN)
- `Matplotlib` – For prediction plotting
- `scikit-learn` – Feature processing and auxiliary ML tasks

### 🤖 AI Models
- **GNN (Graph Neural Network)**: Understands graph structure to identify potential deadlock cycles.
- **LSTM (Long Short-Term Memory)**: Time-series prediction model to anticipate deadlocks based on resource allocation history.
- **Hybrid Prediction**: A custom weighted ensemble of GNN and LSTM models for maximum prediction accuracy.

### 🧮 Algorithms
- **Cycle Detection** using DFS to detect real-time deadlocks
- **Deadlock Prediction** using past patterns in graph evolution
- **OCR Parsing** using Tesseract to extract text and structure from screenshots

---

## 🧪 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yashrao11/AI-Powered-Deadlock-Detection.git
cd AI-Powered-Deadlock-Detection

# 🏀 NBA Player Similarity Search

An interactive web app that allows users to find NBA players with statistically similar profiles based on 2025 season per-game data. Built with **Streamlit**, **scikit-learn**, **PCA**, and **k-NN**, the app also features a 2D interactive visualization of player embeddings using **Plotly**.

---

## 📌 Features

- 🔍 **Similarity Search**: Select any player and retrieve the top-N most statistically similar players using k-Nearest Neighbors.
- 📊 **Dimensionality Reduction**: Applies PCA to reduce player stats to a lower-dimensional space while retaining key variance.
- ⚙️ **Preprocessing Pipeline**:
  - Cleans raw Basketball-Reference data
  - Filters duplicate entries (e.g., multi-team rows)
  - Fills missing values and standardizes all features
- 🚀 **Deployment Ready**:
  - Run locally with Streamlit
  - Easily deployable to [Streamlit Cloud](https://streamlit.io/cloud) or Docker-ready for platforms like Render or AWS

---

## 📁 Project Structure
nba-similarity-search/
├── app.py # Main Streamlit UI
├── utils.py # Data cleaning, PCA, and k-NN logic
├── 2025.csv # Cleaned per-game NBA stats from 2025
├── requirements.txt # Python dependencies
└── Dockerfile # (Optional) for Docker-based deployment

---
## 🔧 Requirements
- Python 3.8+
- Streamlit
- Pandas
- Scikit-learn

---
## 🐳 Run with Docker
```
docker build -t nba-similarity-search .
docker run -p 8501:8501 nba-similarity-search 
```

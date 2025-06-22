import streamlit as st
import pandas as pd
from utils import (
    load_and_prepare_data,
    preprocess_with_scaler,
    reduce_dimensions,
    fit_knn_model,
    get_similar_players
)

# --- Title ---
st.title("🏀 NBA Player Similarity Search")
st.caption("Compare players using 2025 season stats (unsupervised, PCA-reduced)")

# --- Load & preprocess data ---
@st.cache_data
def prepare_all():
    df = load_and_prepare_data('2025.csv')
    df_scaled, _ = preprocess_with_scaler(df)
    df_pca, _ = reduce_dimensions(df_scaled, n_components=10)
    knn = fit_knn_model(df_pca, n_neighbors=11)
    return df, df_pca, knn

df_raw, df_pca, knn_model = prepare_all()

# --- UI: Player selection ---
selected_player = st.selectbox("Select a player to find similar ones:", df_raw.index.sort_values())
top_n = st.slider("Number of similar players", 1, 10, 5)

# --- Run similarity search ---
if st.button("Find Similar Players"):
    results = get_similar_players(selected_player, df_pca, knn_model, top_n=top_n)
    
    if results:
        st.subheader(f"Top {top_n} players similar to **{selected_player}**:")
        for name, score in results:
            st.markdown(f"- **{name}** — Similarity Score: `{score:.3f}`")
    else:
        st.warning("Player not found or insufficient data.")

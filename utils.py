import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors

def load_and_prepare_data(csv_path='2025.csv'):
    df = pd.read_csv(csv_path)
    df = df.iloc[:-1]  # remove footer

    # keep only 1 row per player (the 'TM' version)
    df = df.drop_duplicates(subset='Player', keep='first')

    # drop unwanted columns
    drop_cols = ['Rk', 'Age', 'Team', 'Pos', 'G', 'GS', 'MP', 'FG', 'FGA',
                 'eFG%', 'FT', 'FTA', 'FT%', 'PF', 'Awards', 'Player-additional']
    df = df.drop(columns=drop_cols)

    # set player as index and fill missing values
    df = df.set_index('Player')
    df.fillna(0.0, inplace=True)

    return df

def preprocess_with_scaler(df):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(scaled, index=df.index, columns=df.columns)
    return df_scaled, scaler

def reduce_dimensions(df_scaled, n_components=10):
    pca = PCA(n_components=n_components)
    reduced = pca.fit_transform(df_scaled)
    df_pca = pd.DataFrame(reduced, index=df_scaled.index, columns=[f'PC{i+1}' for i in range(n_components)])
    return df_pca, pca

def fit_knn_model(df_pca, n_neighbors=6):
    knn = NearestNeighbors(n_neighbors=n_neighbors, metric='cosine')
    knn.fit(df_pca)
    return knn

def get_similar_players(player_name, df_pca, knn_model, top_n=5):
    if player_name not in df_pca.index:
        return []
    
    vec = df_pca.loc[player_name].values.reshape(1, -1)
    distances, indices = knn_model.kneighbors(vec, n_neighbors=top_n + 1)
    
    similar_indices = indices[0][1:]  # skip player entered
    similarity_scores = 1 - distances[0][1:]  

    return list(zip(df_pca.index[similar_indices], similarity_scores))

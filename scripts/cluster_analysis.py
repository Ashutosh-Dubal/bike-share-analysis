import pandas as pd
import folium
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from branca.element import MacroElement, Template

save_folder="visuals/cluster"
os.makedirs(save_folder, exist_ok=True)

# Setup for prettier plot
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load data
df_original = pd.read_csv("data/processed/stations_with_coords_clean.csv")

# Pastel-friendly color palette
colors = ['#FF9999', '#99CCFF', '#99FF99', '#FFCC99', '#CC99FF', '#FFFF99', '#66CCCC', '#FFB6C1', '#C0C0C0', '#CCE5FF', '#FFDAB9', '#E6E6FA']

# Container to store cluster assignments
all_clusters_df = pd.DataFrame()

# Store values
inertias = []
silhouette_scores = []
K = range(4, 13)

for k in K:
    df = df_original.copy()

    # Run KMeans
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=12)
    df["cluster"] = kmeans.fit_predict(df[["latitude", "longitude"]])
    centroids = kmeans.cluster_centers_

    # Save inertia
    inertias.append(kmeans.inertia_)

    # Compute silhouette score (only if k > 1)
    score = silhouette_score(df[["latitude", "longitude"]], df["cluster"])
    silhouette_scores.append(score)

    # Append to combined CSV export
    df_k = df[["station_name", "latitude", "longitude", "cluster"]].copy()
    df_k["k"] = k
    all_clusters_df = pd.concat([all_clusters_df, df_k], ignore_index=True)

    # Create folium map
    m = folium.Map(location=[43.65, -79.38], zoom_start=12, tiles="CartoDB positron")

    # Plot station markers
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=4,
            color=colors[row["cluster"] % len(colors)],
            fill=True,
            fill_opacity=0.8,
            weight=1,
            popup=f"<b>Station:</b> {row['station_name']}<br><b>Cluster:</b> {row['cluster']}"
        ).add_to(m)

    # Plot centroid markers and radius
    for i, (lat, lon) in enumerate(centroids):
        # Center marker
        folium.Marker(
            location=[lat, lon],
            popup=f"Centroid {i}"
        ).add_to(m)

    legend_html = f"""
<div style="
    position: fixed; 
    bottom: 30px; left: 30px; width: 180px; 
    background-color: white;
    border: 2px solid grey;
    z-index:9999;
    font-size: 12px;
    padding: 10px;
    border-radius: 8px;">
    <strong>Cluster Legend (k={k})</strong><br>
    {''.join([f"<span style='color:{colors[i % len(colors)]}'>■</span> Cluster {i}<br>" for i in range(k)])}
</div>
"""
    macro = MacroElement()
    macro._template = Template(legend_html)
    m.get_root().add_child(macro)

    # Save the map
    m.save(os.path.join(save_folder, f"clusters_k{k}_styled.html"))
    print(f"Saved: visuals/cluster/clusters_k{k}_styled.html")

# Export all assignments
os.makedirs("data/processed/cluster", exist_ok=True)
all_clusters_df.to_csv("data/processed/cluster/station_clusters_all_k.csv", index=False)
print("Cluster assignments saved: data/processed/cluster/station_clusters_all_k.csv")

# Plotting Inertias values
plt.plot(K, inertias, 'o-', color='orange')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertias')
plt.title('The Elbow Method using Inertias')
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "elbow_method_using_inertias.png"))
plt.clf()

# Plotting Silhouette Score Plot
plt.plot(K, silhouette_scores, 'o-', color='green')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score vs K')
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "silhouette_score.png"))
plt.clf()

print("Cluster plots are saved to visuals folder")
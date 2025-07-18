import pandas as pd
import folium
import os
import seaborn as sns
import matplotlib.pyplot as plt
from branca.colormap import LinearColormap
from folium.plugins import HeatMap

save_folder="visuals/spatial"
os.makedirs(save_folder, exist_ok=True)

# Load trip data and station location data
trips = pd.read_csv("data/processed/bikeshare_2023_combined.csv")
stations = pd.read_csv("data/stations_with_coords_clean.csv")

# Normalize station names
trips["start_station_name"] = trips["start_station_name"].str.strip().str.lower()
trips["end_station_name"] = trips["end_station_name"].str.strip().str.lower()
stations["station_name"] = stations["station_name"].str.strip().str.lower()

# Calculate trip counts
start_counts = trips["start_station_name"].value_counts()
end_counts = trips["end_station_name"].value_counts()

# Combine into a balance dataframe
station_balance = pd.DataFrame({
    "starts": start_counts,
    "ends": end_counts
}).fillna(0)

station_balance["net_flow"] = station_balance["starts"] - station_balance["ends"]
station_balance["total_activity"] = station_balance["starts"] + station_balance["ends"]
station_balance = station_balance.reset_index().rename(columns={"index": "station_name"})

# Merge coordinates
station_balance = station_balance.merge(stations, on="station_name", how="left")
station_balance = station_balance.dropna(subset=["latitude", "longitude"])

# Create heatmap
m = folium.Map(location=[43.65, -79.38], zoom_start=12, tiles="CartoDB positron")

# Heatmap uses total activity for intensity
heat_data = [
    [row["latitude"], row["longitude"], row["total_activity"]]
    for _, row in station_balance.iterrows()
]

HeatMap(heat_data, radius=6, blur=3, max_zoom=14).add_to(m)

# Save
m.save(os.path.join(save_folder, "station_usage_heatmap.html"))
print("Heatmap saved: visuals/spatial/station_usage_heatmap.html")

m2 = folium.Map(location=[43.65, -79.38], zoom_start=12, tiles="CartoDB positron")

# Set up diverging colormap centered at 0
vmax = station_balance["net_flow"].abs().max()
station_balance["normalized_flow"] = station_balance["net_flow"] / vmax  # Range: -1 to 1

vmin = station_balance["normalized_flow"].min()
vmax = station_balance["normalized_flow"].max()

colormap = LinearColormap(colors=["red", "purple", "blue"], vmin=vmin, vmax=vmax, caption="Net Flow (Export → Import)")

# Add colored circle markers based on net flow
for _, row in station_balance.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=7,
        color=colormap(row["normalized_flow"]),
        fill=True,
        fill_color=colormap(row["normalized_flow"]),
        fill_opacity=0.6,
        weight=0,
        popup=f"<b>{row['station_name'].title()}</b><br>Net Flow: {row['net_flow']:.0f}"
    ).add_to(m2)

# Add color legend to map
colormap.add_to(m2)

m2.save(os.path.join(save_folder, "net_flow_map.html"))
print("Heatmap saved: visuals/net_flow_map.html")

def classify_location_type(name):
    name = name.lower()
    if any(kw in name for kw in ["north york", "scarborough", "etobicoke", "eglinton", "kipling", "kennedy", "finch"]):
        return "Suburban"
    else:
        return "Downtown"

station_balance["location_type"] = station_balance["station_name"].apply(classify_location_type)
summary = station_balance.groupby("location_type")[["starts", "ends", "total_activity"]].sum().reset_index()
print(summary)

# Plotting
plt.figure(figsize=(10, 6))
sns.histplot(
    station_balance["net_flow"],
    bins=30,
    kde=True,
    color="skyblue",
    edgecolor="black"
)

plt.axvline(0, color='red', linestyle='--', linewidth=1.5, label="Net Zero")
plt.title("Distribution of Net Bike Flow Across Stations")
plt.xlabel("Net Flow (Starts - Ends)")
plt.ylabel("Number of Stations")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "net_flow_distribution.png"))

print("Spatial plots are saved to visuals folder")
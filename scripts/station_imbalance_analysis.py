import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

save_folder = "visuals/station_imbalance"
os.makedirs(save_folder, exist_ok=True)

# Load the cleaned combined CSV
DATA_PATH = "data/processed/bikeshare_2023_combined.csv"
df = pd.read_csv(DATA_PATH)

df["start_station_name"] = df["start_station_name"].str.strip().str.lower()
df["end_station_name"] = df["end_station_name"].str.strip().str.lower()

start_counts = df["start_station_name"].value_counts()
end_counts = df["end_station_name"].value_counts()

station_balance = pd.DataFrame({
    "starts" : start_counts,
    "ends" : end_counts
}).fillna(0)

station_balance["net_flow"] = station_balance["starts"] - station_balance["ends"]
station_balance["total_activity"] = station_balance["starts"] + station_balance["ends"]

top_exporters = station_balance.sort_values(by="net_flow", ascending=False).head(10)
top_importers = station_balance.sort_values(by="net_flow", ascending=True).head(10)

# Exporters
plt.figure(figsize=(10, 6))
sns.barplot(x=top_exporters["net_flow"], y=top_exporters.index, palette="Blues_d")
plt.title("Top 10 Stations: More Trips Started Than Ended (Exporters)")
plt.xlabel("Net Flow (Starts - Ends)")
plt.ylabel("Station Name")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "top_station_exporters.png"))
plt.clf()

# Importers
plt.figure(figsize=(10, 6))
sns.barplot(x=top_importers["net_flow"], y=top_importers.index, palette="Reds_d")
plt.title("Top 10 Stations: More Trips Ended Than Started (Importers)")
plt.xlabel("Net Flow (Starts - Ends)")
plt.ylabel("Station Name")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "top_station_importers.png"))
plt.clf()

print("Station imbalance plots are saved to visuals folder")
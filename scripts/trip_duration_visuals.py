import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

save_folder = "visuals/trip_duration"
os.makedirs(save_folder, exist_ok=True)

# Setup for prettier plot
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load the cleaned combined CSV
DATA_PATH = "data/processed/bikeshare_2023_combined.csv"
df = pd.read_csv(DATA_PATH)

print(f"Original shape: {df.shape}")
df.dropna(inplace=True)
print(f"New shape after dropping NaNs: {df.shape}")

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("__", "_")
)

print(f"Data Loaded: {df.shape[0]:,} rows, {df.shape[1]} columns")
print("Columns: ", list(df.columns))

# Convert to datatime
df["start_time"] = pd.to_datetime(df["start_time"], errors="coerce")
df["end_time"] = pd.to_datetime(df["end_time"], errors="coerce")

# Add time-related features
df["hour"] = df["start_time"].dt.hour
df["day_of_week"] = df["start_time"].dt.day_name()
df["month"] = df["start_time"].dt.month_name()

# Convert trip_duration to minutes
df["trip_duration_min"] = df["trip_duration"] / 60
filtered_df = df[df["trip_duration_min"] <= 120]

plt.figure(figsize=(10, 6))
sns.histplot(filtered_df["trip_duration_min"], bins=60, kde=False, color="skyblue")
plt.title("Trip Duration Distribution (All Users)")
plt.xlabel("Trip Duration (minutes)")
plt.ylabel("Number of Trips")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trip_duration_histogram_all.png"))
plt.clf()

plt.figure(figsize=(10, 6))
sns.kdeplot(data=filtered_df, x="trip_duration_min", hue="user_type", common_norm=False)
plt.title("Trip Duration KDE by User Type")
plt.xlabel("Trip Duration (minutes)")
plt.ylabel("Density")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trip_duration_kde_usertype.png"))
plt.clf()

plt.figure(figsize=(8, 6))
sns.boxplot(data=filtered_df, x="user_type", y="trip_duration_min")
plt.title("Trip Duration by User Type")
plt.xlabel("User Type")
plt.ylabel("Trip Duration (minutes)")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trip_duration_boxplot_usertype.png"))
plt.clf()

# Group and aggregate
avg_duration = (
    filtered_df.groupby(["day_of_week", "user_type"])["trip_duration_min"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(data=avg_duration, x="day_of_week", y="trip_duration_min", hue="user_type", order=day_order)
plt.title("Average Trip Duration by Day and User Type")
plt.xlabel("Day of Week")
plt.ylabel("Avg Trip Duration (minutes)")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "avg_trip_duration_by_day_user.png"))
plt.clf()

print("Trip duration plots are saved to visuals folder")
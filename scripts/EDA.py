import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

save_folder = "visuals/eda"
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

print("Null start time:", df["start_time"].isna().sum())

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

sns.histplot(df["trip_duration"] / 60, bins=100, kde=True)
plt.title("Trip Duration Distribution (minutes)")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Trips")
plt.xlim(0, 60)
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trip_duration_dist.png"))
plt.clf()

sns.countplot(x="hour", data=df, order=sorted(df["hour"].dropna().unique()))
plt.title("Trips by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Trips")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trips_by_hour.png"))
plt.clf()

sns.countplot(x="day_of_week", data=df, order=day_order)
plt.title("Trips by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Trips")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trips_by_day.png"))
plt.clf()

sns.countplot(x="user_type", data=df)
plt.title("Trips by User Type")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "user_type_breakdown.png"))
plt.clf()

top_stations = df["start_station_name"].value_counts().nlargest(10)
sns.barplot(y=top_stations.index, x=top_stations.values)
plt.title("Top 10 Start Stations")
plt.xlabel("Number of Trips")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "top_start_stations.png"))
plt.clf()

sns.countplot(x="month", data=df, order=month_order)
plt.title("Trips by Month")
plt.xlabel("Month")
plt.ylabel("Number of Trips")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trips_by_month.png"))
plt.clf()

df["route"] = df["start_station_name"] + " -> " + df["end_station_name"]
top_routes = df["route"].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_routes.values,
            y=top_routes.index,
            hue=top_routes.index,
            palette="viridis",
            dodge=False,
            legend=False)
plt.title("Top 10 Most Frequent Bike Routes")
plt.xlabel("Number of Trips")
plt.ylabel("Route")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "top_10_routes.png"))
plt.clf()

plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    x="day_of_week",
    hue="user_type",
    order=day_order,
    palette="Set2"
)
plt.title("Trips by Day of the Week (Grouped by User Type)")
plt.xlabel("Day of Week")
plt.ylabel("Number of Trips")
plt.legend(title="User Type")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trips_by_day_user_type.png"))
plt.clf()

months_to_keep = ["January", "February", "March", "April", "May", "June", "July", "August"]
filtered_df = df[df["month"].isin(months_to_keep)]

plt.figure(figsize=(12, 6))
sns.countplot(
    data=filtered_df,
    x="month",
    hue="user_type",
    order=months_to_keep,
    palette="Set2"
)

plt.title("Trips by Month (Grouped by User Type)")
plt.xlabel("Month")
plt.ylabel("Number of Trips")
plt.legend(title="User Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trips_by_month_user_type.png"))
plt.clf()

plt.figure(figsize=(12, 6))
sns.countplot(
    data=df,
    x="hour",
    hue="user_type",
    palette="Set2"
)

plt.title("Trips by Hour of Day (Grouped by User Type)")
plt.xlabel("Hour (0–23)")
plt.ylabel("Number of Trips")
plt.legend(title="User Type")
plt.tight_layout()
plt.savefig(os.path.join(save_folder, "trips_by_hour_user_type.png"))
plt.clf()

print("EDA plots are saved to visuals folder")
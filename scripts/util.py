import pandas as pd
import requests
import time

RAW_DATA_PATH = "data/processedbikeshare_2023_combined.csv"
GEO_OUTPUT_PATH = "data/raw/stations_with_coords.csv"
CLEAN_OUTPUT_PATH = "data/processed/stations_with_coords_clean.csv"
USER_AGENT = "Toronto-Bike-Project"

def geocode_station(name):
    """Geocode a station name using OpenStreetMap's Nominatim API."""
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": f"{name}, Toronto, Canada",
            "format": "json",
            "limit": 1
        }
        headers = {"User-Agent": USER_AGENT}
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception as e:
        print(f"Failed to geocode '{name}': {e}")
    return None, None

def extract_unique_stations(path):
    df = pd.read_csv(path)
    stations = pd.concat([df["start_station_name"], df["end_station_name"]]).dropna().unique()
    return pd.DataFrame({"station_name": sorted(stations)})

def geocode_stations(df):
    df["latitude"] = None
    df["longitude"] = None

    for i, row in df.iterrows():
        lat, lon = geocode_station(row["station_name"])
        df.at[i, "latitude"] = lat
        df.at[i, "longitude"] = lon
        print(f"{row['station_name']} → ({lat}, {lon})")
        time.sleep(1)  # Respect rate limit
    return df

def fix_coordinate_format(row):
    try:
        lat_val = str(row["latitude"]).strip()
        lon_val = row["longitude"]

        if "," in lat_val and pd.isna(lon_val):
            lat, lon = lat_val.split(",")
            return float(lat.strip()), float(lon.strip())
        return float(lat_val), float(lon_val)
    except:
        return None, None

def clean_coordinates(df):
    df.columns = df.columns.str.strip().str.lower()
    if "latitude" not in df.columns or "longitude" not in df.columns:
        df["latitude"] = None
        df["longitude"] = None

    df[["latitude", "longitude"]] = df.apply(fix_coordinate_format, axis=1, result_type="expand")
    df = df.dropna(subset=["latitude", "longitude"])
    return df

if __name__ == "__main__":
    print("Extracting unique stations...")
    station_df = extract_unique_stations(RAW_DATA_PATH)

    print("Geocoding station coordinates...")
    station_df = geocode_stations(station_df)
    station_df.to_csv(GEO_OUTPUT_PATH, index=False)
    print(f"Geocoded stations saved to: {GEO_OUTPUT_PATH}")

    print("Cleaning up coordinate formatting...")
    cleaned_df = clean_coordinates(pd.read_csv(GEO_OUTPUT_PATH))
    cleaned_df.to_csv(CLEAN_OUTPUT_PATH, index=False)
    print(f"Cleaned coordinates saved to: {CLEAN_OUTPUT_PATH}")
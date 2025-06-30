import os
import pandas as pd

RAW_DATA_PATH = "data/raw/bikeshare-ridership-2023"
PROCESSED_DATA_PATH = "data/processed"
OUTPUT_FILE = os.path.join(PROCESSED_DATA_PATH, "bikeshare_2023_combined.csv")

def load_all_csvs(raw_path):
    all_files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]
    all_files.sort()  # Sort by name so Jan → Dec

    dataframes = []
    for file in all_files:
        file_path = os.path.join(raw_path, file)
        print(f"📄 Loading {file_path}")
        try:
            df = pd.read_csv(file_path, encoding="utf-8-sig", na_values=["NULL"])
            # df['source_file'] = file  # Optional: tag source file
            dataframes.append(df)
        except Exception as e:
            print(f" Failed to read {file_path}: {e}")

    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

def save_combined_csv(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Saved combined CSV to: {output_path}")

if __name__ == "__main__":
    print("🚴 Combining monthly CSVs into one DataFrame...")
    df = load_all_csvs(RAW_DATA_PATH)
    print(f"🔢 Combined DataFrame shape: {df.shape}")
    save_combined_csv(df, OUTPUT_FILE)
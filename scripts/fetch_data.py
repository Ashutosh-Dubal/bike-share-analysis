import requests
import zipfile
import os


def get_download_url(resource_id):
    """Fetch the actual file download URL from CKAN metadata"""
    api_url = f"https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/resource_show?id={resource_id}"
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    return data['result']['url']


def download_zip_file(resource_id, output_path="data/raw/bikeshare_2023.zip"):
    print("Fetching actual download URL...")
    download_url = get_download_url(resource_id)
    print(f"Downloading from: {download_url}")

    response = requests.get(download_url)
    if response.status_code != 200:
        raise Exception(f"Failed to download file: {response.status_code}")

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"File downloaded to {output_path}")

def extract_zip(zip_path, extract_to="data/raw/"):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted files to {extract_to}")

if __name__ == "__main__":
    resource_id = "f0fa6a67-4571-4dd6-9d5a-df010ebed7d1"
    zip_path = "data/raw/bikeshare_2023.zip"

    if not os.path.exists(zip_path):
        download_zip_file(resource_id, zip_path)
    else:
        print("ZIP file already exists, skipping download.")

    extract_zip(zip_path)

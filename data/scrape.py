import csv
import requests
from bs4 import BeautifulSoup
import os

input_csv_path = 'links.csv'
output_csv_path = 'downloaded_content.csv'
progress_tracker_path = 'progress_tracker.txt'

def save_progress(last_row):
    with open(progress_tracker_path, 'w') as f:
        f.write(str(last_row))

def load_progress():
    try:
        with open(progress_tracker_path, 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0  # Start from the beginning if no progress file found

start_row = load_progress()

with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    urls = list(reader)

# Check if file exists and has content already
file_exists = os.path.isfile(output_csv_path) and os.path.getsize(output_csv_path) > 0

with open(output_csv_path, mode='a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # If the file is being created for the first time, write column names
    if not file_exists:
        writer.writerow(['URL', 'Content'])  # Column names
    
    for index, row in enumerate(urls[start_row:], start=start_row):
        if not row or not row[0]:  # Skip empty rows or rows without a URL
            print(f"Skipping empty or invalid row at index {index}")
            save_progress(index + 1)
            continue

        url = row[0]
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            body_content = soup.body.get_text(separator=' ', strip=True) if soup.body else ''
            
            exclude_text = "Date created:"
            if exclude_text in body_content:
                body_content = body_content.split(exclude_text)[0]
            
            clean_content = body_content.replace('\n', ' ').replace('\r', ' ').strip().rstrip("'").rstrip('"')
            
            writer.writerow([url, clean_content[:10000000]])  # Content limited to fit in cell
            
            save_progress(index + 1)
        except requests.RequestException as e:
            print(f"Error downloading {url}: {e}")
            save_progress(index + 1)

print("Download completed.")
import json
import os

# Define paths
download_path = '/workspaces/replication-of-new-data/dataset'
json_file_path = os.path.join(download_path, 'Electronics_5.json')
output_dir = '/workspaces/replication-of-new-data-set'
output_file_path = os.path.join(output_dir, 'electronics_reviews.txt')

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Check if the source JSON file exists
if not os.path.isfile(json_file_path):
    print(f"Source JSON file {json_file_path} does not exist. Please check the path.")
else:
    # Convert to FastText format
    try:
        with open(json_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
            for line in file:
                try:
                    # Parse each line as a separate JSON object
                    review = json.loads(line.strip())
                    # Extract label and text
                    label = f"__label__{review['overall']}"
                    text = review['reviewText'].replace('\n', ' ')
                    # Write in FastText format
                    output_file.write(f"{label} {text}\n")
                except json.JSONDecodeError as e:
                    print(f"Skipping line due to JSON decode error: {e}")
        print("Dataset prepared for FastText at:", output_file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")

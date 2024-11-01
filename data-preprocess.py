import json
import os

# Define the actual download path for the unzipped data
download_path = '/home/codespace/.cache/kagglehub/datasets/shivamparab/amazon-electronics-reviews/versions/1'
json_file_path = os.path.join(download_path, 'Electronics_5.json')
output_file_path = '/workspaces/replication-of-new-data-set/electronics_reviews.txt'

# Convert to FastText format
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

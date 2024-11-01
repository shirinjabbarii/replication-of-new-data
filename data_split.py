import random
import os

# Create the directory if it does not exist
output_dir = '/workspaces/Application-of-data-final-report/fastText'
os.makedirs(output_dir, exist_ok=True)

# Correct file paths
train_file_path = os.path.join(output_dir, 'train.ft.txt')
test_file_path = os.path.join(output_dir, 'test.ft.txt')

# Load the preprocessed file
source_file = '/workspaces/replication-of-new-data-set/electronics_reviews.txt'
with open(source_file, 'r') as file:
    lines = file.readlines()

# Shuffle and split into train and test
random.shuffle(lines)
split_point = int(0.8 * len(lines))
train_lines = lines[:split_point]
test_lines = lines[split_point:]

# Save to train and test files within the correct directory
with open(train_file_path, 'w') as train_file:
    train_file.writelines(train_lines)

with open(test_file_path, 'w') as test_file:
    test_file.writelines(test_lines)

print("Train and test files created in:", output_dir)

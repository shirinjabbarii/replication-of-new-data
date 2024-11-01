import fasttext

# Paths to train and test files
train_file = '/workspaces/Application-of-data-final-report/dataset/train.ft.txt'
test_file = '/workspaces/Application-of-data-final-report/dataset/test.ft.txt'

# Train the FastText model
model = fasttext.train_supervised(input=train_file)

# Test the model with test file
results = model.test(test_file)
print(f"Test Results - Precision: {results[1]}, Recall: {results[2]}")

# Save the model for future use
model.save_model("/workspaces/Application-of-data-final-report/dataset/fasttext_model.bin")

print("Model training and testing complete.")

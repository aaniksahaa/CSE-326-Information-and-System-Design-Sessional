import os
import json

# Folder containing the JSON files
folder_path = 'db'  # Replace with the actual path to your folder

# List to hold merged data
merged_data = []

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):  # Ensure it's a JSON file
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)  # Load JSON data
            merged_data.extend(data)  # Add to the merged list

# Save the merged data to a new JSON file
with open('db-merged.json', 'w') as output_file:
    json.dump(merged_data, output_file, indent=4)

print("All JSON files merged into 'db-merged.json'.")

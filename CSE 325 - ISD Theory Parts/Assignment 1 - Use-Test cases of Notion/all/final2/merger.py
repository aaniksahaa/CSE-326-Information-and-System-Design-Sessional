import json
import os

# List of JSON files in the correct order
file_names = [
    "1-Workspace Management.json",
    "2-Content Management.json",
    "3-Database Creation and Management.json",
    "4-Sharing and Collaboration.json",
    "5-Plans and Payment.json",
    "6-Third Party Integration.json"
]

author_student_ids = [
    "2005023",
    "2005013",
    "2005017",
    "2005001",
    "2005006",
    "2005012"
]

# Path to the folder containing the JSON files
folder_path = "./"

# Start with an empty list to hold the merged data
merged_data = []

# Iterate over each file in the specified order
for i, file_name in enumerate(file_names):
    author_student_id = author_student_ids[i]
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        # Load the JSON data (assuming it's an array) and extend the merged list
        data = json.load(f)
        for d in data:
            d['usecase']['author_student_id'] = author_student_id
        merged_data.extend(data)

# Path to save the merged JSON file
output_path = os.path.join(folder_path, "A1-4_Notion.json")

# Write the merged list to a new JSON file
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, indent=4)

print(f"Merged JSON saved to {output_path}")

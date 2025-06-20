import json
import os

def convert_numbers_to_strings(data):
    if isinstance(data, dict):
        return {k: convert_numbers_to_strings(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_numbers_to_strings(item) for item in data]
    elif isinstance(data, (int, float)):
        return str(data)
    return data

def preprocess_biospecimen_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        converted_data = convert_numbers_to_strings(data)
        preprocessed_filename = file_path.replace('raw_data', 'preprocessed_data')

        with open(preprocessed_filename, 'w') as outfile:
            json.dump(converted_data, outfile, indent=4)

        print(f"Preprocessed data saved to {preprocessed_filename}")


if __name__ == "__main__":

    file_path = './raw_data/biospecimen.project-tcga-lgg.2025-06-14.json'
    preprocess_biospecimen_data(file_path)

    print("Data has been preprocessed.")
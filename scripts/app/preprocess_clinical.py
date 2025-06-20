import pandas as pd
import os

def preprocess_clinical_data(file_path):
    for file in os.listdir(file_path):
        if file.endswith('.tsv'):
            print(f"Processing {file}...")
            df = pd.read_table(os.path.join(file_path, file), sep='\t', low_memory=False)
            if len(df) == 0:
                continue
            df.replace({"'--": None}, inplace=True)
            # drop columns with all NaN values
            df.dropna(axis=1, how='all', inplace=True)
            preprocessed_filename =  f'./preprocessed_data/{file.replace(".tsv", ".csv")}'
            df.to_csv(preprocessed_filename, index=False)
            print(f"Preprocessed {file} and saved to {preprocessed_filename}")

def preprocess_biospecimen_data(filename):
    # placeholder
    pass


if __name__ == "__main__":

    file_path = './raw_data/clinical.project-tcga-lgg.2025-06-14/'

    preprocess_clinical_data(file_path)

    print("All files have been preprocessed.")
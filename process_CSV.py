import os
import argparse
import pandas as pd

def process_csv_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name)
            process_csv_file(input_file_path, output_file_path)

def process_csv_file(input_file_path, output_file_path):
    # Read CSV file and select only 'blast_hit' and 'num_reads' columns
    data = pd.read_csv(input_file_path)
    selected_columns = ['blast_hit', 'num_reads']
    processed_data = data[selected_columns]
    processed_data.to_csv(output_file_path, index=False)

def main():
    parser = argparse.ArgumentParser(description="Process CSV files")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing CSV files")
    parser.add_argument("output_folder", type=str, help="Path to the folder to save the processed CSV files")
    args = parser.parse_args()

    process_csv_files(args.input_folder, args.output_folder)
    print("Processing complete.")

if __name__ == "__main__":
    main()

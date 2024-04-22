import os
import argparse
import pandas as pd

def merge_csv_files(input_folder, output_file):
    all_data = []

    # Iterate over all CSV files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            barcode = os.path.splitext(file_name)[0]  # Extract barcode from file name
            input_file_path = os.path.join(input_folder, file_name)
            data = pd.read_csv(input_file_path)
            data['Barcode'] = barcode  # Add a 'Barcode' column to identify the source
            all_data.append(data)

    # Concatenate all dataframes into one
    merged_data = pd.concat(all_data, ignore_index=True)

    # Save the merged dataframe to a CSV file
    merged_data.to_csv(output_file, index=False)

def main():
    parser = argparse.ArgumentParser(description="Merge CSV files into one")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing CSV files")
    parser.add_argument("output_file", type=str, help="Path to the output merged CSV file")
    args = parser.parse_args()

    merge_csv_files(args.input_folder, args.output_file)
    print("Merge complete.")

if __name__ == "__main__":
    main()

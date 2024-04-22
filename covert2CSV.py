import os
import argparse
import pandas as pd

def convert_xlsx_to_csv(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".xlsx"):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name.replace(".xlsx", ".csv"))
            convert_file_to_csv(input_file_path, output_file_path)

def convert_file_to_csv(input_file_path, output_file_path):
    # Read Excel file and write to CSV
    data = pd.read_excel(input_file_path)
    data.to_csv(output_file_path, index=False)

def main():
    parser = argparse.ArgumentParser(description="Convert .xlsx files to .csv files")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing .xlsx files")
    parser.add_argument("output_folder", type=str, help="Path to the folder to save the converted .csv files")
    args = parser.parse_args()

    convert_xlsx_to_csv(args.input_folder, args.output_folder)
    print("Conversion complete.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python

import os
import argparse
import shutil

def main(input_directory, output_directory):
    # Ensure input directory exists
    if not os.path.isdir(input_directory):
        print("Error: Input directory does not exist.")
        return

    # Iterate over files in input directory
    for file_name in os.listdir(input_directory):
        if file_name.endswith(".fastq") or file_name.endswith(".fastq.gz"):
            # Extract barcode from filename
            name = file_name.split('-')[2]
            print("Processing {}".format(name))

            # Create output directory for barcode
            output_subdirectory = os.path.join(output_directory, name)
            os.makedirs(output_subdirectory, exist_ok=True)

            # Copy file to output directory
            input_path = os.path.join(input_directory, file_name)
            output_path = os.path.join(output_subdirectory, file_name)
            shutil.copy(input_path, output_path)

    print('Finished processing.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort fastq files or fastq.gz files into barcode-specific folders.")
    parser.add_argument("input_directory", type=str, help="Path to input directory containing fastq files")
    parser.add_argument("output_directory", type=str, help="Path to output directory where barcode-specific folders will be created")
    args = parser.parse_args()

    main(args.input_directory, args.output_directory)

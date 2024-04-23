# GermGenie
pipeline for a stacked barplot after MABA 16S is finished

# Installing MABA16s
### Create an environment for snakemake
```
conda create --name smk Snakemake 
```

```
`conda activate smk`
```

### Install MABA16S
do this in the direction you would like to install MABA16S in (for instance your programs folder)

```
git clone https://github.com/MUMC-MEDMIC/MABA16S
```

To overcome any issues with Snakemake locking it's own files preventing the pipeline frow working we will need to change a small part in the snake file:

`CD` into: `/MABA16S/maba16s/` (if advise was followed, located in your programs folder)

open the snake file: 
```
nano Snakefile
```
Scroll down in the file and add "nolock

### Make an alias to be able to run from home directory
```
echo "alias MABA='/path/too/MABA16S/maba16s/cli.py snakemake'"  >> ~/.bashrc
```

Make sure to change the first part

restart the terminal: 
```
source ~/.bashrc
```

### installing script for processing MABA16S output

```
git clone https://github.com/daanbrackel/GermGenie
```
Keep in mind that this will put the scripts in a GermGenie folder.

You can also manually install all python scripts in the same directory, for instance a programs folderd.

you can download the list of below scripts from this repository and upload them to your programs folder or create them yourself by using nano "file_name.py", and copy pasting the script.

- convert2CSV.py

- process_CSV.py

- merge_CSV_MABA16s.py

- plot_MABA16s.py
  
# Running MABA 

Start by running the following commandline:

```
MABA --cores 8 -i input/* -o output
```
the input should be replaced with a folder containing a barcode folder that holds a fastq.gz file of the barcode. The output should be a folder of your choice (recommended to use a name similar to the run name). The cores can be changed by your liking.

input folder structure:

![image](https://github.com/daanbrackel/MABA16s_after_process/assets/127868974/5b460540-0d40-4835-8a5e-41d3e5b0e1dc)


# running the script for processing the output of MABA16s

- start of by running the convert2CSV.py script. you can do this as followed (assuming your in the GermGenie directorie where all scripts are located):

  ```
  python covert2CSV.py "input_folder" "output_folder"
  ```

  the input folder is the the "report" folder you get as output from MABA16s

  or enter 

  ```
  python convert2CSV.py --help
  ```

  for an explenation what each in/output is.

- next run process_CSV.py:

  ```
  python process_CSV.py "input_folder" "output_folder"
  ```

  the input folder is the path to the folder containing the the new CSV files (your previous output folder). choose the output folder by your own for instance "csv_processed".

  or enter 

  ```
  python process_CSV.py --help
  ```

  for an explenation what each in/output is.

- now merge all barcodes into one dataframe:

  ```
  python merge_CSV_MABA16s.py "input_folder" "output_file"
  ```

  the input folder is the path to the folder containing the the new processed CSV files (your previous output folder, "csv_processed"). for the output place it in a directory don't forget to put .csv behind you file name.

  or enter 

  ```
  python merge_CSV_MABA16s.py --help
  ```

  for an explenation what each in/output is.

- finally visualize all your data in a plot:

  ```
  python plot_MABA16s.py "input_csv" "output_species.html"
  ```

  the input is the newly merged CSV file you just made. the output can be put in a directory of you choosing, but don't forget to put ".html" behind the name.

  or enter 

  ```
  python plot_MABA16s.py --help
  ```

  for an explenation what each in/output is.

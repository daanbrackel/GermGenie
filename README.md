# GermGenie
pipeline for a stacked barplot and a table that contains the total reads, classified reads and the abundance percentage per species (after MABA16S is finished). it is based on the report folder filled with .xlxs files per barcode. these files contain the amount of reads per species for each barcode.

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
nano cli.py
```
Scroll down in the file and replace the entire part below "parsing part" with the following text:
```

    args = parser.parse_args(command_line)
    if args.mode == "rename":
        renamer(
                input_file=args.input_directory,
                spreadsheet=args.spreadsheet
                )

    elif args.mode == "snakemake":
        snakemake_in(
                samples=args.input_files,
                outdir=args.outdir,
                )

        os.chdir(f"{locationrepo}")

        if args.smkparams == None:
            args.smkparams=""
        exitstatus = os.system(f"snakemake --cores {args.cores} --nolock --use-conda {args.smkparams} --snakefile Snakefile_check_suitable_sample>
        if exitstatus > 0:
            sys.exit("pre-workflow crashed")
        os.system(f"snakemake -p --cores {args.cores} --use-conda {args.smkparams} --nolock --notemp --keep-going")

    else:
        parser.print_usage()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
```

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
Keep in mind that this will put the script in a GermGenie folder.

**Make sure any additional deppendencies are installed as well:**
```
pip install pandas
```
```
pip install openpyxl
```
```
pip install plotly
```
  
# Running MABA 

Start by running the following commandline:

```
MABA --cores 8 -i input/* -o output
```
the input should be replaced with a folder containing a barcode folder that holds a fastq.gz file of the barcode. The output should be a folder of your choice (recommended to use a name similar to the run name). The cores can be changed by your liking.

input folder structure:

![image](https://github.com/daanbrackel/MABA16s_after_process/assets/127868974/5b460540-0d40-4835-8a5e-41d3e5b0e1dc)


# running the script for processing the output of MABA16s

- start of by running the genies_lamp.py script. you can do this as followed (assuming your in the GermGenie directorie where the scripts is located):

  ```
  python genies_lamp.py "input_folder" "output_folder"
  ```

  the input folder is the the "report" folder you get as output from MABA16s, containing all .xlxs files. the output folder can be any folder desired by the user.

  or enter 

  ```
  python genies_lamp.py --help
  ```

  for an explenation what each in/output is.

Your output folder should now contain all document that where needed to creat your plot (the .html file)

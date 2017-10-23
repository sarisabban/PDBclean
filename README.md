# PDBclean
A small script that cleans the PDB database

## Requirements:
Use the following command (in GNU/Linux) to install all nessesary programs and Python libraries for this script to run successfully:

`sudo apt install python3-pip && sudo pip3 install biopython`

## How To Use:
Use the following command to run the script (~72 hours):

`python3 PDBclean.py SMALLER_THAN LARGER_THAN`

SMALLER_THAN LARGER_THAN means delete all proteins that are less than SMALLER_THAN amino acids in size and larger than LARGER_THAN amino acids in size.

The script will start by downloading the PDB database which will take around ~72 hours and occupy ~27GB in size.

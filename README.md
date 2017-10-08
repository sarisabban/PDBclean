# PDBclean
A small script that cleans the PDB database

## Requirements:
1. Use the following command (in GNU/Linux) to install all nessesary programs and Python libraries for this script to run successfully:

`sudo apt install python3-pip && sudo pip3 install biopython`

2. Download the PDB database using this command (~72 hours and ~27GB):

`rsync -rlpt -v -z --delete --port=33444 rsync.wwpdb.org::ftp/data/structures/divided/pdb/ ./DATABASE`

## How To Use:
Use the following command to run the script (~72 hours):

`python3 PDBclean.py`

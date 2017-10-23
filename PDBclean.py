#!/usr/bin/python3

import gzip , os , Bio.PDB.Polypeptide , Bio.PDB.PDBParser

#Collect Structures
os.system('rsync -rlpt -v -z --delete --port=33444 rsync.wwpdb.org::ftp/data/structures/divided/pdb/ ./DATABASE')
current = os.getcwd()
os.mkdir('PDBDatabase')
filelist = os.listdir('DATABASE')
for directories in filelist:
	files = os.listdir(current + '/DATABASE/' + directories)
	for afile in files:
		location = (current + '/DATABASE/' + directories + '/' + afile)
		print(location)
		os.rename(location , current + '/PDBDatabase/' + afile)
os.system('rm -r ./DATABASE')
#Separate Chains
pdbfilelist = os.listdir('PDBDatabase')
for thefile in pdbfilelist:
	#Open File
	TheFile = current + '/PDBDatabase/' + thefile
	TheName = TheFile.split('.')
	#Extract Each Chain and Save as Different Files
	InFile = gzip.open(TheFile, 'rb')
	for line in InFile:
		line = line.decode()
		if line.startswith('ATOM') or line.startswith('ANISOU'):
			chain = line[21]
			Name = TheName[0].split('pdb')
			output = open(Name[1] + '_' + chain + '.pdb' , 'a')
			output.write(line)
			output.close()
	os.remove(TheFile)
#Remove Unwanted Structures
pdbfilelist = os.listdir('PDBDatabase')
for thefile in pdbfilelist:
	TheFile = current + '/PDBDatabase/' + thefile
	structure = Bio.PDB.PDBParser(QUIET=True).get_structure('X' , TheFile)
	ppb = Bio.PDB.Polypeptide.PPBuilder()
	Type = ppb.build_peptides(structure)
	#Delete Non-Protein Files
	if Type == []:
		print('[-] NOT PROTEIN\t' , thefile)
		os.remove(TheFile)
	else:
		#Delete Structures Larger Than 150 or Smaller Than 100 Amino Acids
		length = int(str(Type[0]).split()[2].split('=')[1].split('>')[0])
		if length > 150 or length < 100:
			print('[-] WRONG SIZE\t' , thefile)
			os.remove(TheFile)
		else:
			print('[+] GOOD\t' , thefile)

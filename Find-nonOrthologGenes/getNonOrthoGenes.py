#!/usr/bin/python
## This is to get the list of genes (from table of complete set of genes) in isolates that had no ortholog associated with them compared to the reference (from the result of Proteinortho) 
## NOTE test.* files are only a subset of real data! 
## Depends on which non-orthologs you want to find, you need to adjust the file and lists' number within this script 

import sys

output = sys.stdout
f = open("result-nonOrtho-genes.tab", "w")  ##e.g. This is to find non-orthologs of reference sclerotinia vs sclerotinia L angustifolius
sys.stdout = f

mut_orthoDict = {}
ang_orthoDict = {}

with open("test.proteinortho", "r") as file1:
	for line in file1:
		if "#" not in line:
			la = line.strip().split('\t') 
			if ('*' not in la[3]) and ('*' not in la[5]): ### change la[3] to la[4] to get the same for mutabilis
				if ',' in la[3]:
					for i in la[3].split(','): ## This is to take into the account where there is paralog
						mut_orthoDict[i] = la[5]
				else:
					mut_orthoDict[la[3]] = la[5]
#print mut_orthoDict	


with open("test-tableOfGenes.tab", "r") as file:
	for line in file:
		ll = line.strip().split('\t')
		if ll[0] not in mut_orthoDict:
			print '\t'.join(ll)

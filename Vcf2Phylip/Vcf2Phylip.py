#!/usr/bin/python
## Usage: python Vcf2Phylip.py
## It will change a vcf file in a format of "test.vcf" to "infile" which is input fileformat of PHYLIP.
## Warnings: it only works for biallelic SNPs.  

import sys
import numpy as np

stdout = sys.stdout
f=open('infile', 'w')
sys.stdout=f
id = []
ind_dict = {}

with open('test.vcf', 'r') as file:
	for line in file:
		if '#CHROM' in line:
			fl=line.split()
			acc=fl[9:]
			lenAcc=len(acc)
		elif '#' not in line:
			ll=line.split()
			marker=ll[2]
			ref=ll[3]
			alt=ll[4]
			geno=ll[9:]
			newGeno=[]
			id.append(marker)
			marker=id
			for i in geno:
   				if i == '0/0':   
					i = ref 
				elif i == '1/1':
					i = alt
				else:
					assert i != '2/2'
					i = "-" 
				newGeno.append(i)
			geno=newGeno
			if not ind_dict:
				for ind in acc:
					ind_dict[ind] = []
			
			for ind, allele in zip(acc, geno):
				ind_dict[ind].append(allele)	
print str(lenAcc) + '   ' + str(len(marker))
for i in ind_dict:
	print  i.ljust(50,' ') + ''.join(ind_dict[i])
sys.stdout = stdout
f.close()

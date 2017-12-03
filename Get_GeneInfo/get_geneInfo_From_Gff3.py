#!/usr/bin/python

## this is to get the column of interest from gff3 file of reference genome of Scl1980 (gene informations)

import sys
import re

output = sys.stdout
f = open("result_test.tab", "w")
sys.stdout = f

print ("CHR\tgeneStart\tgeneEnd\torientation\tgeneLength\tgeneName")

with open("test.gff3", "r") as file1:
	
	for line in file1:
		sline = []
		if "#" not in line:
			ll = line.strip().split('\t')
		#	if "gene" in ll[2]:  Remember this one also find lines with ncr_gene which I don't want, so instead I used the re function to find exact matches of 'gene'
			if re.match('gene', ll[2]):
				sline.append(ll[0])   #chr name
				sline.extend(ll[3:5])  #gene start end position
				sline.append(ll[6])  #seq orientation
				sline.append(str(float(ll[4])-float(ll[3]))) #gene length   NOTE:float to be able to do arithmetic and str to be able to print it with join

				desc = [i.split("=") for i in ll[8].split(";")]  
				try:
					desc = dict(desc)
				except:
					print(line)
					sys.exit(1)

				sline.append(desc["gene_id"]) #get value of Name which are my gene's name
				
		
				print '\t'.join(sline)

#!/usr/bin/python

'''  This is to count number of UNIQUE genes in each pfam domain from a table which has the following columns, extracted from interproscan output file:
 geneid   start   end     pfam_name       pfam_id
This code get the Output file produced by 0a_ExtractPfamDomain-fromInterproscanOutput.py and give the count of unique genes in each pfam domain '''



import sys
output = sys.stdout
f = open('output_0b.tab', 'w')
sys.stdout = f

with open("outputfile_0a.tab", "r") as file:
	Mydict={} # I want to make a dictionary with pfam ids as key and genes as values
	for line in file:
		ll=line.strip().split("\t")
		geneid=ll[0]  # this is my dict value
		pfamid=ll[4] # this is my dict key
		Mydict.setdefault(pfamid, []).append(geneid) # setdefault will allow me to have different values for the same key
	
	for pfamid, geneid in Mydict.items():
		numGene = len(set(geneid))  #This will count number of unique genes in each pfam domain
		print str(pfamid) + '\t' + str(numGene)

sys.stdout = output
f.close()

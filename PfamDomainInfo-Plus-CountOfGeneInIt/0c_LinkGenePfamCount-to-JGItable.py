#!/usr/bin/python
''' This is to link two tables whith the same pfamid to add the "number of gene count in each pfam domain" to the bigger table with more pfam ids.
I had a big table with other pathogens pfam info, 'Noheader_PfamVsGenomes_0c.txt' (pfam 0 to 17225) and I wanted to get my pfam count in the same order to add it to that table.  
Please note that the example files are a very small representative of the real dataset, so it may make more sense when you try this script on your own data!
 '''

import sys
 
output = sys.stdout
f = open('output_0c.tab', 'w')
sys.stdout = f	

myDict={}

with open("output_0b.tab") as file2:
	for line in file2:
		ll = line.strip().split('\t')
		myDict[ll[0]] = ll[1] # making a dictionary in which pfamid is key and number of genes in that domain are values 

with open("Noheader_PfamVsGenomes_0c.txt") as file1:
	for line in file1:
		c = line.strip().split('\t')
		if c[0] in myDict:  # if pfam id in file1 also exist in my dictionary 
	#		print c[0], myDict[c[0]]  # then print pfamid from file1 and ring up its value from dictionary
			print str(c[0]) + '\t' + str(myDict[c[0]])
		else:
	#		print c[0], 0 # if it doesn't find a match pfam id then put 0 as value for those
			print str(c[0]) + '\t' + '0'
sys.stdout = output
f.close()

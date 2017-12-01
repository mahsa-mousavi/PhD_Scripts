#!/usr/bin/python

import sys 

output = sys.stdout
f = open("test_dnds.1.tab", "w")
sys.stdout = f 


with open("test.tab", "r") as file:
	print "geneName	dN	dS	ratio"

	for line in file:
		if '#' not in line:
			ll = line.strip().split("\t")
			geneID = ll[0]
			dn = float(ll[2])
			ds = float(ll[3])
			
			if ds > 0:
				ratio = dn/ds
				print str(geneID) + '\t'+ str(dn) + '\t' + str(ds) + '\t'+ str(ratio)
			else:
			
				print str(geneID) + '\t'+ str(dn) + '\t'+ str(ds) + '\t' + "NA"
	

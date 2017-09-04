#!/usr/bin/python

'''  This is to extract the info from interproscan gff3 output file containing pfam only. Check test_0a.gff3 for inputfile example.
 Usage: python 0a_ExtractPfamDomain-fromInterproscanOutput.py
 It produce outputfile_0a.tab '''  

import re
import sys

with open("test_0a.gff3", "r") as file: 

	output = list()
	for line in file:
		sline = [] # geneid, start, end, pfamid, pfamname
		ll=line.strip().split("\t")
		sline.append(ll[0])
		sline.extend(ll[3:5])
		
		desc=[x.split("=", 1) for x in ll[8].split(";")]
		try: # use try and except to get the first line that cause  error message and then kill the program
			desc = dict(desc)
		except:
			print(line)
			sys.exit(1)

		sline.append(desc["signature_desc"])
		pfid = re.sub("PF", "pfam", desc["Name"])
		sline.append(pfid)
		output.append(sline)

with open("outputfile_0a.tab", "w") as handle:
	handle.write("geneid\tstart\tend\tpfam_name\tpfam_id\n")
	for line in output:
		handle.write("\t".join(line) + "\n")


#!/usr/bin/python
### I want to get the gene information and functions for regions with coverage below 30% (link gene  table info with coverage table) 

import sys
output = sys.stdout
f = open("results-filteredPAV-function.02.tab", "w")
sys.stdout = f

myDict = {}

print("geneName\tCHR\tgeneStart\tgeneEnd\torientation\tgeneLength\teffectorP\tsignalP\tcazym\tpfam\tCov-below30-in1IsolateAtleast")

with open("result_coverageTable_FilterStat.01.tab", "r") as file1:
	for line in file1:
		la = line.strip().split('\t')
		if 'yes' in la[5]:
			myDict[la[0]] = la[5]
#print myDict

with open("test-tableOfGenes.tab", "r") as file:
	for line in file:
		ll = line.strip().split('\t')
		if ll[1] in myDict:
			print '\t'.join(ll) + '\t' + myDict[ll[1]]

#!/usr/bin/python
### This is to add an additional column to identify if coverage in any of the isolates was <= 0.30

import sys

output = sys.stdout
f = open("result_coverageTable_FilterStat.01.tab", "w")
sys.stdout = f

print("#Scaff\tlength\tRefBcin_coverage\tbcinT4_coverage\tbcinBcdw_coverage\tstatus")

with open("test.tab", "r") as file:
	for line in file:
		if "#" not in line:
			ll = line.strip().split('\t')
			bcinRef = float(ll[2])
			bcinT4 = float(ll[3])
			bcinBcdw = float(ll[4])

			if (bcinRef <= 0.30)  or (bcinT4 <= 0.30) or (bcinBcdw <= 0.30):
				print '\t'.join(ll) + '\t' + 'yes'
			else:
				print '\t'.join(ll) + '\t' + 'no'

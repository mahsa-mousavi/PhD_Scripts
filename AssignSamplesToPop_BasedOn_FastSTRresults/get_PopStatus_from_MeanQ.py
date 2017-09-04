#!/usr/bin/python

#USAGE: python get_PopStatus_from_MeanQ.py test.meanQ > OutPutfile_name.PopStatus

import sys
import itertools

myfile=open(sys.argv[1], 'r') #will read the file which we specify on keyboard
ADMIX = "Admixed"
CUT_OFF = 0.7

for line in myfile:
    ll = line.rstrip('\n').split()
    biggest = 0
    biggest_counter = 0
    position = 1
    for element in ll:
        number = float(element)
        if number > biggest:
            biggest = number
	    biggest_counter = position
        position += 1
    if biggest < CUT_OFF:
        cluster = ADMIX
    else:
        cluster = biggest_counter
    ll.append(str(cluster))
    print '\t'.join(ll)

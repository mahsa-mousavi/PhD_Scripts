#!/usr/bin/python

#USAGE: python PhaseGenoFile.py test > OutPut_Name.tab
#NOTE:This script is for phasing the genotypes relative to the parents. In other words, if the mother is '1', then replace all '1' scores in the RILs with an 'A'. If the mother is '0', then replace all '0' scores with an 'A'. Same for the father but replace with a 'B'


import sys

myfile=open(sys.argv[1], 'r') #will read the file which you specify on keyboard
mother = "A"   #Store values in variables
father = "B"

for line in myfile:    #will read the file line by line, will split it by tab, and store our values in list 
    ll = line.rstrip('\n').split('\t')
    marker = ll[0]
    MOTHER = ll[1]
    FATHER = ll[2]
    Genotypes = ll[3:]
	
    for index, element in enumerate(Genotypes): #this will go through every element of a list
  	if FATHER in element:
	   Genotypes[index] = father
 	elif MOTHER in element:					   
	   Genotypes[index] = mother
        elif '999' in MOTHER and '-' not in element:
           Genotypes[index] = mother
    print marker + '\t' + MOTHER + '\t' + FATHER + '\t' + '\t'.join(Genotypes)


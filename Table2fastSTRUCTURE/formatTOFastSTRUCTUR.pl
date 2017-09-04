#!/usr/bin/perl

#### Usage: perl formatToFastSTRUCTURE.pl test

# This is to change format of a table similar to "test" to the format recognizable by fastStructure program. My file already had the missing values shown as -9, so this code doesn't take that into account. This will produce a file "import_to_fastSTR.str", which can be import to fastStructure. 




use strict;

open (OUT, ">import_to_fastSTR.str") or die "error crating result.txt";

while (<>) {
chomp;
my @data = split(/\t/);
my @data2 = @data; #make a copy of my array

	splice (@data, 1, 0, 'g', 'g', 'g', 'g', 'g');
	splice (@data2, 1, 0, 'g', 'g', 'g', 'g', 'g');		
		map(tr/2/0/, @data[1..$#data]);	# I exclude the first element of my array (my sample names) from the replacemnt operation
		map(tr/2/1/, @data2[1..$#data2]); 
	
print OUT "@data\n"; 	
print OUT "@data2\n"; 	


}


close,


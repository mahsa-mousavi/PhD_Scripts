### to claculate dn/ds ratio I first extracted different columns of my need from snpEff output file _gene.txt
### However to see the number of those columns I used this awk command first: awk 'BEGIN{ FS="\t" } { for(fn=1;fn<=NF;fn++) {print fn" = "$fn;}; exit; }' test_gene.txt > ColumnNumber.txt      

###### For some of the files the position of column I wanted was different. Make sure to double check this if u are doing this steps again ###########


awk -F '\t' -v OFS='\t' '{print $1,$2,$17,$26,$19,$20,$22,$23}' test_genes.txt > test.tab
awk -F '\t' -v OFS='\t' '{print $1,$2,$16,$25,$18,$19,$21,$22}' 0aa_snpEff_genes.txt > 0aa_Scl1980-vs-SclHom_ImportantSummary.tab
awk -F '\t' -v OFS='\t' '{print $1,$2,$17,$26,$19,$20,$22,$23}' 0b_snpEff_genes.txt > 0b_Scl1980-vs-myMutab_ImportantSummary.tab
awk -F '\t' -v OFS='\t' '{print $1,$2,$17,$26,$19,$20,$22,$23}' 0c_snpEff_genes.txt > 0c_Scl1980-vs-myAngus_ImportantSummary.tab
awk -F '\t' -v OFS='\t' '{print $1,$2,$20,$30,$23,$24,$26,$27}' 0d_snpEff_genes.txt > 0d_Refbcin-vs-myBcin_ImportantSummary.tab
awk -F '\t' -v OFS='\t' '{print $1,$2,$20,$30,$23,$24,$26,$27}' 0e_snpEff_genes.txt > 0e_Refbcin-vs-bcdwBcin_ImportantSummary.tab
awk -F '\t' -v OFS='\t' '{print $1,$2,$20,$30,$23,$24,$26,$27}' 0f_snpEff_genes.txt > 0f_Refbcin-vs-t4Bcin_ImportantSummary.tab


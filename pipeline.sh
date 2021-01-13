F=genome.fasta
# K=31

for K in 63
do
   
	### FOR DOUBLE DIRECTED
	dsk -file $F -kmer-size $K -abundance-min 1 -out dskcount.h5
	dsk2ascii -file dskcount.h5 -out kmersascii.txt
	./jellyfish count -m $K -s 100M -t 10 $F
	./jellyfish dump -c mer_counts.jf > mer_counts_dumps.fa


	#cat kmersascii.txt | cut -f 1 -d"" \; > fwd_kmer.txt
	cat mer_counts_dumps.fa | cut -f 1 -d" " > kmersascii_fwd.txt
	cat mer_counts_dumps.fa | cut -f 1 -d" "  | tr ACGTacgt TGCAtgca | rev > kmersascii_rev.txt
	cat kmersascii_fwd.txt kmersascii_rev.txt | sort | uniq | awk '{print $0" 1"}'  > kmers_all.txt

	cat kmersascii_fwd.txt | cut -f 1 -d" " | awk '{print ">\n" $0}' > fwdkmers.txt
	cat kmersascii_rev.txt | cut -f 1 -d" " | awk '{print ">\n" $0}' > bwdkmers.txt

	./bcalm  kmers_all.txt dd.unitigs 2
	# BCALM/bcalm  mer_counts_dumps.fa dd.unitigs 2


	cat dd.unitigs | tr a A | tr c C | tr g G | tr t T | tr -d \; > fwd.txt
	cat fwd.txt | tr ACGTacgt TGCAtgca | rev > rev.txt
	cat fwd.txt rev.txt | sort | uniq | cut -f 1 -d" " | awk '{print ">contig\n" $0}' > ddcontig$K.fa

	# #cat fwd.txt | sort | uniq | cut -f 1 -d" " | awk '{print ">contig\n" $0}' > ddcontig$K.fa


	# ### FOR BIDIRECTED
	 bcalm -minimizer-size 1 -in $F  -kmer-size $K -abundance-min 1 -out bidi.unitigs.fa
	cat bidi.unitigs.fa.unitigs.fa | sed '/^>/d'  > bidi_fwd
	cat bidi_fwd | tr ACGTacgt TGCAtgca | rev > bidi_rev
	cat bidi_fwd bidi_rev | sort | uniq | cut -f 1 -d" " | awk '{print ">contig\n" $0}' > bdcontig$K.fa
done






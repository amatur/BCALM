
def revcomp(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
    return reverse_complement

file = open("genome.txt")
G = file.read()
G = G.upper()
G = G.replace("\n", "")
file.close()

Gwrite=">contig\n"+G
Gbar_write=">contig\n"+revcomp(G)

text_file = open("lastfirst.fa", "w")
n = text_file.write(Gwrite)
text_file.close()

text_file = open("lastfirst_bar.fa", "w")
n = text_file.write(Gbar_write)
text_file.close()


# k=31
# Gbar=revcomp(G)

# if True:
#     ktimesn="N" * k
#     first=G[0:k-1]
#     last=G[-(k-1):]
#     G2 = G.replace(first, ktimesn)
#     G2 = G2.replace(last, ktimesn)
#     print(revcomp(first))
#     print(revcomp(last))
#     splits=G2.split(ktimesn)
#     print(splits)
#     print(len(splits))

#     # for x in range(len(splits)):
#     #      print(x, splits[x])
#     # x = txt.split(", ")

# #check if all strings are substring
# # open other file in write mode 

# FILENAME="bdcontig"+str(k)+".fa"
# ddcontig = open(FILENAME, 'r') 

# # read the content of the file line by line 
# cont = ddcontig.readlines() 
# type(cont) 
# for i in range(0, len(cont)):
#     if(i % 2 != 0): 
        
#         if not (cont[i].strip() in G or cont[i].strip() in Gbar):
#             print("false", cont[i].strip())
#             #print()
#     else: 
#         pass
  
# # close the file 
# ddcontig.close() 
# print("h")
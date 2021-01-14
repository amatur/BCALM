
import sys 
def revcomp(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
    return reverse_complement

def checkPalindrome(s):
    return s==revcomp(s)

K = sys.argv[1]
bdfilename="bdcontig"+K+".fa"
ddfilename="ddcontig"+K+".fa"


file = open(bdfilename) #check all unitigs of this file
G = file.read()
G = G.upper()
G = G.replace(">contig\n", "")
file.close()

ddcontig = open(ddfilename, 'r') 
bdcontig = open(bdfilename, 'r') 

# read the content of the file line by line 
cont = ddcontig.readlines()  # see if differs with this
type(cont) 
for i in range(0, len(cont)):
    if(cont[i]==">contig\n"):
        pass
    elif not (cont[i].strip() in G):
        print(checkPalindrome(cont[i].strip()), cont[i].strip())
        #print()
    else: 
        pass
  
# close the file 
ddcontig.close()
bdcontig.close() 
print("Finish!")

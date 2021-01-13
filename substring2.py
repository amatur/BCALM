
def revcomp(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
    return reverse_complement

def checkPalindrome(s):
    return s==revcomp(s)

file = open("sorted_b20.txt")
G = file.read()
G = G.upper()
#G = G.replace("\n", "")
file.close()

FILENAME="sorted_d20.txt"
ddcontig = open(FILENAME, 'r') 

# read the content of the file line by line 
cont = ddcontig.readlines() 
type(cont) 
for i in range(0, len(cont)):
    if not (cont[i].strip() in G):
        print(checkPalindrome(cont[i].strip()), cont[i].strip())
        #print()
    else: 
        pass
  
# close the file 
ddcontig.close() 
print("h")
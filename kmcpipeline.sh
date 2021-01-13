./kmc -fa -k31 -b -ci1 fwdkmers.txt  NA.res  data/
./kmc -fa -k31 -b -ci1 bwdkmers.txt  NAbar.res  data/
./kmc_tools simple  NA.res NAbar.res intersect intersectNA
./kmc_dump intersectNA outputint.txt
./kmc_dump NA.res fwdkmc.txt     
./kmc_dump NAbar.res bwdkmc.txt




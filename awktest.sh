awk  -F  " " '{print ($1==$2?""$1" M":_)}' column.txt | awk 'NF' > match.txt

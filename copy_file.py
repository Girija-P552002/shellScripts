src="text.txt"
dest="file2.txt"

with open (src,'r') as src1:
  content=src1.read()
  
with open(dest,'w') as dest1:
  dest1.write(content)  
   

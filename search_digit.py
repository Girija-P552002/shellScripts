import re
pattern =r'\d'
txt='this is the year 2024'
match=re.search(pattern,txt)
if match:
 print("match found",match.group())
else:
 print("match not found")  

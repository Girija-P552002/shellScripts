import re
pattern =r'h..lo'
txt='girija'
match=re.search(pattern,txt)
if match:
     print("Match found",match.group())
else:
    print("match not found")     


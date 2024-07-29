import re
pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})',re.VERBOSE)
txt='today\'s date is 15/07/2023'
matchs =re.search(pattern,txt)
if matchs:
  day, month, year=matchs.groups()
  print(day,month,year)
else:
  print("no match")

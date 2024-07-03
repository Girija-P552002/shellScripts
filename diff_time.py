from datetime import datetime
def diff(date1,date2):
  diff = date2-date1 
  print(f"Time difference :{diff}")
  
date1=datetime(2024,1,1)
date2=datetime(2024,2,1)
diff(date1,date2) 

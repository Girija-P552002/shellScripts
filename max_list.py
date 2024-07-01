#find the maximum element in the list
def find_max(l):
  max_num=l[0]
  for i in range(0,len(l)):
    if max_num < l[i]: 
      max_num=l[i]
  return max_num    
     
l=[4,9,6,7,11]
result=find_max(l)

print(result)  
  

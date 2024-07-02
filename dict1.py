#remove the element from dict
dict1={'name':'girija','age':22,'day':'monday','date':'01-07-2024'}
keys=['name','date']
for i in keys:
    dict1.pop(i)
print(dict1) 



dict2={'a':2,'f':4,'c':5,'d':6}
print("im printing only keys")
for i in dict2.keys(): 
    print(f"keys:{i}")
    
print("im printing only values")
for i in dict2.values(): 
    print(f"values:{i}")    

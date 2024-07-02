#dict operations
#convert the list into dictionary

name=['anu','thanu','abhi','varsha']
age=[22,12,28,18]
result=dict(zip(name,age))
print(result)

# merge two dict
dict1={'mon':1,'tue':2}
dict2={'wed':3,'thur':4}
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)

#print the value of the keys from the nested dict

dict4={'class':{'student':{'marks':{'devops':50,'communication':60}}}}
print(dict4['class']['student']['marks']['devops'])
 


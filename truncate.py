 
import os 

path = "/home/girija/Desktop/practice/text.txt"
print("File size", os.path.getsize(path))  
length = 72
os.truncate(path, length) 
print("Content of file Python_intro.txt:") 
with open(path, 'r') as f: 
	print(f.read()) 
print("File size", os.path.getsize(path)) 


#performing all file handling operations
import os
with open('abc.txt','r') as file:
  content=file.read()
print(content)

with open('abc.txt','w') as file:
   file.write("hello")
   
with open('file.txt', 'a') as file:
    file.write('\nAppending new line.')
   
if os.path.exists('abc1.txt'):
    print('file path exists')
else :
    print('file path does not exists')    
      

import os
def list_files(dir):
   with os.scandir(dir) as files:
     for i in files:
       print(i)
list_files("/home/girija/Desktop/pss")
       

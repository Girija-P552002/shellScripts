f=open('/home/girija/Desktop/pss/my_log.log','r')
lines = f.readlines()
for line in lines:
	kern_log = line.split()
	print(kern_log)

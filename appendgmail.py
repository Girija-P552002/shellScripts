data=[
     {"USN":"1DA20IS011","name":"girija","Domain":"Devops","gmail":"girija@ambertag.com"},
     {"USN":"1DA20IS012","name":"anu","Domain":"AI","gmail":None},
     {"USN":"1DA20IS013","name":"thanu","Domain":"ML","gmail":None},
     {"USN":"1DA20IS014","name":"divya","Domain":"ML","gmail":None},
     {"USN":"1DA20IS015","name":"teju","Domain":"AI","gmail":""},
     {"USN":"1DA20IS016","name":"kavya","Domain":"AI","gmail":None},

]
print(f"{'USN'}\t\t{'name'}\t{'Domain'}\t\t{'gamil'}")
for i in data:
        print(f"{i['USN']}\t{i['name']}\t{i['Domain']}\t{i['gmail']}")

print("--------------generating mail ID------------------")

# def fun(name,gmail):
#     if [gmail==""]:
#         print(f"{name}user not entered the mail ID ");
#     elif[gmail==None]:
#         print(f"{name}user not entered the mail ID ");
#     else:
#         print(f"{name}user has entered mail ID");

def fun1(name):
    # print("generate an email if not present")
    return f"{name}@ambertag.com"

for i in data:
    if not i["gmail"]:
        i["gmail"]=fun1(i["name"])

def printing(data):
    print(f"{'USN'}\t\t{'name'}\t{'Domain'}\t\t{'gamil'}")
    for i in data:
        print(f"{i['USN']}\t{i['name']}\t{i['Domain']}\t{i['gmail']}")
# fun('name','gmail') 
printing(data) 
   

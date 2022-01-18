menu="""
1.istifadeci daxil et
2.istifadeciler 
3.istifadecileri sil
4.menuyunu goster
5.cix
"""
print(menu)


def adduser():
        print("adduser")
def User():
        print("users")
def deleteuser():
        print("sil")

        
while True:
    emr=input("emri daxil et:")
    if eval(emr)==1:
        adduser()
    elif eval(emr)==2:
        User()
    elif eval(emr)==3:
        deleteuser()
    elif eval(emr)==4:
        print(menu)
    elif eval(emr)==5:
        break
        
        
     

   
    
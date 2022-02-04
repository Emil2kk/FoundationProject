a=[]
b=[]
class Info:
    def __init__(self,username,password):
        self.username=input()
        self.password=int(input())
       
    def register(self):
        a.append(self.username)
        b.append(self.password)
        if self.username in a :
            print("siz artiq qeydiyyatdan kecmisiz")
    
first=Info("salam",23)
first.register()

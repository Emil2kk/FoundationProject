from random import randint
kartkodu= "2002-2002-2002-2002"
kartid="4567"
bitistarixi="24/12"
pul=input("pulun:")

maincard={
    "kartkodu":kartkodu,
    "kartid":kartid,
    "bitistarixi":bitistarixi,
    "pul":pul
}
print(maincard)

class Virtualcard:
    def __init__(self,kod,id,tarix,vpul):
        self.kod=randint(1000,9999),-randint(1000,9999),-randint(1000,9999),-randint(1000,9999)
        self.id=randint(1000,9999)
        self.vpul=int(input("verilen pulu daxil et:"))
        self.tarix=input("bitistarixi: yy/mm  ")
        
        
            
        
    def generateCode(self):
        if self.vpul >int(pul):
            print("daxil olunan mebleg yoxdur")
        elif eval(bitistarixi)<eval(self.tarix):
            print("verilen tarix esas kardin bitis tarixinden cox ola bilmez")
        else:
            print("kartkodu:",self.kod ,"kartid:",self.id ,"daxil olunan pul:",self.vpul,"bitistarixi:",self.tarix)
            qalanpul=int(pul)-self.vpul
            print("qaliq:",qalanpul)  
        

card1=Virtualcard(12,12,12, 12)     
card1.generateCode()
pul=input("pulun:")
card2=Virtualcard(13,14,15, 16)  
card2.generateCode()  
              

    
    



    
        


        

        
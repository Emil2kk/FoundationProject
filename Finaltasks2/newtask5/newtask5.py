menu='''
 qeydiyyatdan kecmek ucun [1] yazin:
 -istifadeci adiniz:
 -istifadeci parolu:
 sisteme daxil olmaq ucun [2] yazin
 ana menyuya qayitmaq ucun [3] yazin
sistemden cixmaq ucun [4] yazin
 
'''

print(menu)
secim = int(input('Seciminizi daxil edin: '))
users =[]
passwords=[]
class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        users.append(self.username)  
        passwords.append(self.password)
        
    def showuserdata(self):
        print(f'{self.username} siz artiq qeydiyyatdan kecmisiniz')

while True:
    if secim == 1:
        username=input('-Istifadeci adiniz: ')
        password=input('-Parolunuz: ')
        user= User(username, password)
        print('Qeydiyyatdan kecdiniz')
        
        secim = int(input('Seciminizi daxil edin: '))     
    if secim==2:
        username=input('-Istifadeci adiniz: ')
        password=input('-Parolunuz: ')
        user= User(username, password)
        if user.username in users and user.password in passwords:
           user.showuserdata()
        elif user.username not in users :
           print('Qeydiyyatdan kecmemisiniz!')
        secim = int(input('Seciminizi daxil edin: '))
    if secim == 3:
        print(menu) 
        secim = int(input('Seciminizi daxil edin: '))

    if secim ==4:
       break

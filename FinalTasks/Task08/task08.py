#The Minion Game
strg = input() 
vowel = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
nonwowel=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'z','B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
x = "" 
count=0 
point=0
for i in strg:
    x+=i
    for z in x : 
        if z in vowel:
            count+=1
    for b in x:
        if b in nonwowel:
           point+=1 
            
   
if count>point:
    print("bob",count)
    
else:
    print('Emil',point)

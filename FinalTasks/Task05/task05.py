#Words Score
vowel = ['a', 'e', 'i', 'o', 'u','y']
Sen = input("cumle daxil et: ")
print(Sen.split())
score=0
for word in Sen.split():
    count = 0
    for z in word:
        if z in vowel:
           count+=1
    if count%2==0 :
        score+=2
    else :
        score+=1
        
print(score)
        
    
    

        
            

arr=['Samir','Mehemmed','Qurbani','Vesile','Qurbaneli','Memmedaga','Nurlan','Leman','Emil','Gulshen']

e=[]
for z in arr:
    b= len(z)
    e.append(b)
    if len(z)==max(e):
        print(z)
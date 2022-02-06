from re import I
from countries import olkeler
city=input()
def FindCity(cityname):
   Countries = list(olkeler.keys())
   cities = list(olkeler.values())
   for x in range(len(Countries)):
    for y in range(len(cities)):
      if cityname in cities[y] and x==y:
       print(f'{cityname} -' ,Countries[x])
  
   pass

def FindCountry(countryname):
   if countryname in olkeler.keys():
    cities = olkeler.get(countryname) 
    print(f'{countryname} -' ,cities)
    pass

def CityCountMax():
 Countries = list(olkeler.keys())
 cities = list(olkeler.values())
 countcity=[]
 maxcity=0
 for x in range(len(cities)):
   countcity.append(len(cities[x])) 
   maxcity=max(countcity)   
   maxindex = countcity.index(maxcity) 
 print(Countries[maxindex])
 pass

def CountAllCities():
  count=0
  city=list(olkeler.values())
  for x in range(len(olkeler.values())):
    count += len(city[x])       
  print(count)
  
  pass

FindCity(city)
FindCountry(city)
CityCountMax()
CountAllCities()
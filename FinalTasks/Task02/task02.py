#Find Angle MBC
import math
try:
    a=int(input('eded :'))
    b=int(input('eded :'))
    c=math.sqrt(a*a+b*b)

    d=c/2

    print (round(math.degrees((math.asin(d/b)))))
    
except ValueError:
    print("Terefler qaydasina uygun terefleri qeyd edin")
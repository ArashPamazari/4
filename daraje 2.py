import math 

def daraje2( a, b, c): 

    delta = b **2 - 4 * a * c 
    moadele = math.sqrt(abs(delta)) 
      
    if delta > 0: 
        print("rishe motefavet:") 
        print((-b + moadele)/(2 * a)) 
        print((-b - moadele)/(2 * a)) 
      
    elif delta == 0: 
        print("rishe yeksan:") 
        print(-b / (2 * a)) 
      
    else:
        print("rishe mobham:") 
        print(- b / (2 * a), " + ", moadele) 
        print(- b / (2 * a), " - ", moadele) 
  
a = int(input('meghdar a ra vared konid: '))
b = int(input('meghdar b ra vared konid: '))
c = int(input('meghdar c ra vared konid: '))
  
if a == 0: 
        print("moadele javab nadarad") 
  
else:
    daraje2(a, b, c)
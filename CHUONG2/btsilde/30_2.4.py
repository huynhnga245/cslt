a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
import math
S=(a+b+c)/2
Dientich=math.sqrt(S*(S-a)*(S-b)*(S-c))
print('Dien tich=', Dientich)
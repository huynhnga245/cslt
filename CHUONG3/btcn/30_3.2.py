a=int(input('M1='))
b=int(input('M2='))
c=int(input('M3='))
S=(int(input('S=')))
if S<100: d=a*S
elif S<=150: d=100*a+(S-100)*b
else:  d=100*a+(S-150)*c+50*b
print('Phai tra=',d, sep='')
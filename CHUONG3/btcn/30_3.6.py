a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and c+b>a:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a: print('Tam giac vuong')
    elif a==b and b==c and a==c: print('Tam giac deu')  
    else: print('Tam giac loai khac')  
else: print('Khong hop le')
T=float(input())
L=float(input())
H=float(input())
ĐTB=(H+T*2+L*3)/6
if 9<=ĐTB<10: print('Xuat sac')
elif 8<=ĐTB<9: print('Gioi')
elif 7<=ĐTB<8: print('Kha')
elif 6<=ĐTB<7: print('Trung binh kha')
elif 5<=ĐTB<6: print('Trung binh')
elif 3<=ĐTB<5: print('Yeu')
else: print('Kem')
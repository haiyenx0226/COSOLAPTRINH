n=int(input('So tien ban dau: '))
k=int(input('So thang gui: '))
t=float(input('Lai suat/thang: '))
print('Voi so tien ban dau ',n,',',' sau ',k,' thang gui,',' lai suat ',str(t),'/thang',sep=(''))
print('Thi so tien nhan duoc cuoi ky la:',n*(1+k*t))
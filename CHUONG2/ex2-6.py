hoten=str(input('Ho ten: '))
songaycong=int(input('So ngay cong: '))
dongiangaycong=int(input('Don gia ngay cong: '))
hesophucap=float(input('He so phu cap: '))
tamung=int(input('Tam ung: '))
luong= dongiangaycong*songaycong*hesophucap
thuclinh=luong-tamung
print('Nhan vien ',hoten,', Co tien Luong=',str(luong),', Tam ung=',str(tamung),' va Thuc linh=',str(thuclinh),sep=('')) 
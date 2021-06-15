#Author:SercanCelenk
#1: Liste elemanlarının sayısal degelerini bul.

''' liste=["1","2","5a","10b","abc","10","50"]
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue #devam et '''

#2 Kullanici 'q' degerini girmedikce aldiginiz
# inputun sayı oldugundan emin olun,
# aksi halde hata mesaji yaziniz.


''' while True:
    sayi=input("sayi:")
    if sayi=='q':
        break

    try:
        result=float(sayi)
    except ValueError:
        print("gecersiz input")
 '''
#3: Girilen parola icinde turkce karakter hatası veriniz.


''' def checkPassword(parola):
    turkce_karakterler="ışçğöİŞÖÇ"


    for x in parola:
        if x in turkce_karakterler:
            raise TypeError('Parola turkce karakter iceremez')
        else:
            pass
    print("parola girisi basarili.!")

parola=input("Parola giriniz")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)
 '''


def faktoriyel(x):
    x=int(x)

    if x <0:
        raise ValueError("Negatif deger!")
    
    result =1

    for i in range(1,x+1):
        result*=i
    
    return result


for x in [5,10,20,-3,'a0']:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue

    print(y)

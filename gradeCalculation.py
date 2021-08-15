def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')

    ogrenciAdi=liste[0]
    notlar=liste[1].split(',')

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama=(not1+not2+not3)/3

    if ortalama>=90 and ortalama<=100:
        harf="AA"
    elif ortalama>=85 and ortalama <=89:
        harf="BA"
    elif ortalama>=65:
        harf="CC"
    else:
        harf="FF"

    return ogrenciAdi+": "+harf+ "\n"    



def notlari_oku():
    with open("sinav_notları.txt","r",encoding='utf-8') as file:
        for satir in file:
            print(not_hesapla(satir))



def not_gir():
    ad=input("Ogrenci Adi: ")
    soyad=input("Ogrenci Soy Adi: ")
    not1=input("Not 1: ")
    not2=input("Not 2: ")
    not3=input("Not 3: ")

    with open("sinav_notları.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+''+not1+','+not2+','+not3+'\n')


def kaydet():
    pass



while True:
    islem=input('1-Notlar Oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Cikis\n')

    if islem=='1':
        notlari_oku()
    elif islem=='2':
        not_gir()
    elif islem=='3':
        kaydet()
    else:
        break
    
        
        

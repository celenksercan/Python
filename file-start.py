#Author:SercanCelenk
#Dosya açmak ve olusturmak için open() fonk. kullanılır.
#Kullanimi: open(dosya_adi,dosya_erisme_modu)

# "w" write yazma modu. Dosyayı konumda olusturur
# "a" append ekleme.    Dosyayı konumda olusturur
# "x" create olusturma  Dosya zaten varsa hata verir
# "r" read okuma    Dosya konumda yoksa hata  verir.


file=open("newfile.txt","a")
file.write("\n172119014")
file.close()
  

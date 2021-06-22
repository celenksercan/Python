#Author:SercanCelenk

""" 
try:
    file=open("newfile.txt")
    print(file)
except FileNotFoundError:
    print("dosya basariyla okundu")
finally:
    file.close()
    print("dosya kapatildi.") """


file=open("newfile.txt","r",encoding="utf-8")


#for dongusu
""" for i in file:
    print(i, end="") """

#read() fonksiyonu

""" content1=file.read()
print("icerik 1")
print(content1)

file=open("newfile.txt","r",encoding="utf-8")
content2=file.read()
print ("icerik 2")
print(content2)
 """

 #readline fonksiyonu
 # her seferinde 1 satır okur.

print(file.readline(),end="")
print(file.readline(),end="")
 

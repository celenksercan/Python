""" 
#sayfa basinda güncelleme
with open("newfile.txt","r+",encoding="utf-8") as file:
    file.write("YENI EKLEME")

with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())
 """


 #sayfa sonuna güncelleme

""" with open("newfile.txt","a", encoding="utf-8") as file:
    file.write("\nSercan Celenk")
    
    
with open("newfile.txt","r", encoding="utf-8") as file:   
    print(file.read()) """

#sayfa basinda guncelleme

""" with open("newfile.txt","r+",encoding="utf-8") as file:
    content=file.read()
    content="Muhammed Bera\n"+content
    file.seek(0)
    file.write(content)

with open("newfile.txt","r", encoding="utf-8") as file:   
    print(file.read()) """


#sayfa ortasinda guncelleme

with open("newfile.txt","r+", encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,'tusem nehir\n')
    file.seek(0)
    for i in list:
        file.write(i)
    # file.writelines(list) de olabilir.
with open("newfile.txt","r", encoding="utf-8") as file:
    print(file.read())








#Author:SercanCelenk
with open("newfile.txt","r",encoding="utf-8") as file:
    content=file.read()
    print(content)
    file.seek(0) #cluser'i istenilen byte'a gönderme
    print(file.tell()) # cluser kacıncı byte'ta




import random

result=random.random() #0 ile bir arasında random sayı üretir.
result=random.uniform(10,100) #10 ile 100 arasında random sayi üretir.


names=["sercan","celenk","dynamic","code"]

""" result1=random.uniform(0,len(names))
result2=int(result1)
print(names[result2]) """

""" result=random.choice(names)

print(result)

liste=list(range(10)) #0'dan 10'a kadar liste oluşturur

random.shuffle(liste) #listeyi karıştırır.
print(liste) """

liste=range(100)
result=random.sample(liste,3)
result=random.sample(names,2)
print(result)
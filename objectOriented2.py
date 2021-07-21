mylist=[1,2,3]

myString='sercan'


print(len(mylist))
print(len(myString))

class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie objesi olusturuldu")

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie silindi.")

m=Movie('sercancelenk',"ALLAH",155)

del m

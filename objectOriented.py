class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("Person created")
    def whoami(self):
        print ("I am a person")

    def eat(self):
        print ("I am a eating")

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        print ("Student created")
        self.studentNumber=number
    def whoami(self):
        print("I am a student")

    def sayHello(self):
        print(f"hello i am a {s1.fname}")


class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch

    def whoami(self):
        print(f"i am a {self.branch} teacher")

p1=Person("sercan","celenk")   
s1=Student("seyma","karakaya",1021)
t1=Teacher("yelda","bayram","maths")
s1.whoami()
p1.eat()
s1.eat()
s1.sayHello()

t1.whoami()


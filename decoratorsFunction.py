#Author:SercanCelenk
def my_decorator(func):
    def wrapper():
        print("fonksiyondan onceki islemler")
        func()
        print("fonksiyon sonraki islemler")
    return wrapper


def sayHello():
    print("hello")


def sayGreeting():
    print('greeting')

sayHello=my_decorator(sayHello)

sayHello()

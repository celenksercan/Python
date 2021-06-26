def cube():
    for i in range(5):
        yield i**3


generator=cube()
iterator=iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
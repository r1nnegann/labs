from random import randint

a = randint(1,50)
b = randint(a,50)

def squares():
    for i in range(a,b+1):
        yield i**2


print(f"a={a}, b={b}")
for i in squares():
    print(i)
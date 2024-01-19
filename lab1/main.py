# python syntax
print("Hello World")

if 5 > 2:
    print("YES")

# python comments

# This is a comment

"""This is a comment
written in 
more than just one line"""

# python Variables
carname = "Volvo"
x = 50
y = 10
print(x + y)
z = x + y
print(z)
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"


def myfunc():
    global x
    x = "fantastic"


# python Data Types
x = 5
print(type(x))  # <class 'int'>

x = "Hello World"
print(type(x))  # <class 'str'>

x = 20.5
print(type(x))  # float

x = ["apple", "banana", "cherry"]
print(type(x))  # list

x = ("apple", "banana", "cherry")
print(type(x))  # tuple

x = {"name": "John", "age": 36}
print(type(x))  # set

x = True
print(type(x))  # bool

# python Numbers
x = 5
x = float(x)

x = 5.5
x = int(x)

x = complex(x)

# python Strings
x = "Hello World"
print(len(x))

txt = "Hello World"
X = txt[0]

x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World".upper()

txt = txt.lower()

txt = "Hello World"
txt.replace("H", "J")

age = 36
print(f"My name is John, and I am {age} years old")


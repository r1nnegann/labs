from math import pi, tan

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
print(f"The area of the polygon is: {(n*l**2)/(4*tan(pi/n))}")
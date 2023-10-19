import math

x = float(input("Введите число x: "))
y = float(input("Введите число y: "))
z = abs((math.cos(x)**3)/(3*math.pi**2)+((math.exp(x*y)+abs(x-y))/y**4))
print(z)
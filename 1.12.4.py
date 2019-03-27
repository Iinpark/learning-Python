form = input ()
if form == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    
    p = (a + b + c)/2
    S = ((p - a)*(p - b)*(p - c) * p) ** 0.5
    print (S)

if form == 'круг':
    r = int(input())
    import math
    S = math.pi * r ** 2
    print(S)

if form == 'прямоугольник':
    a = int(input())
    b = int(input())

    print(a * b)

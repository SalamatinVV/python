import math

print ("Введите коэф для ур:ax^2+bx+c")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
D=(b*b-4*a*c)
if D>0 :
    d = math.sqrt(D)
    print ("x1=", (-b+d)/(2*a))
    print ("x2=", (-b-d)/(2*a))
elif D==0 : print ("x=",-b/2*a )
else :
    print ("Корней нет")



import random

n= random.randint(1, 50)
k= int (input("Кол-во попыток:"))
print ("You can try")
c= int (1)
for i in range (1, k+1):
    print ("попытка", c)
    x = int(input("Print your number:"))
    if x==n :  print ("You win")
    elif x>n : print ("x>n")
    elif x<n : print ("x<n")
    c += 1
print ("You lose, number was" , n)
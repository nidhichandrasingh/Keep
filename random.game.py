import random
n=random.randint(1,50)





#n=34
m=5
print("guess the number that hidden in game ")
print("you have 5 chances only")
print("let's start the game")


while(m>0 ):
    n1 = int(input("\n enter your number:"))
    if n1>n:
        print("\n\nyour number is greater then our number")
        print("you have guess left",m)
    elif n1<n:
        print("\n\nyour number is smaller then our number")
        print("you have guees left",m)
    elif n1==n:
        print("\n\nwinner winner chiken dinner")
        exite()




    m=m-1


print("\n\nyou loss the game")
print("number is =",n)

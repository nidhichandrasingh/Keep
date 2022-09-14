n = 11
print("guess a number hidden in the game ")
print("you have 5 chances only")
print("lets start the game")
m=5
while (m>0):
    m=m-1

    
    a = int(input("enter your number"))
    if a<n:
        print("your number is less then our")
        print("you have left chance only ",m)
    elif a>n:
        print("your number is greater then our number")
        print("you have left chance only",m)
    elif a==n:
        print("yeah you won the game")
        exit()

        
print("you loss the game")
print("our number is  =", n )

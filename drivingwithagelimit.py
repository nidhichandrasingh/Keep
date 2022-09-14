print(" hay guysss")
print(" are you here for driving permission")
n = int(input(" if you wnna continue then press 1"
              " if not then press 2"))
if n==1 :
    
    print("yes you may continue now")
    
elif n==2:
    
     print("As you wish")
     exit()

else:
    print("press 1 or 2 only")
    exit()

    
print(" Enter your age here ")
age = int(input())
if age >18 and age<100:
    print("yuppp you can drive ")

elif age==18:
    print("ummmm have to think about you ")

elif age>6 and age<18:
    print(" i wanna say sorry "
             "but"
                " you cannot drive at any cost")

else :
    print(" ooops not a valid age")

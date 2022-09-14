import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("successfully written")
        elif(c==2):
            value=input("type here\n")
            with open("harry-food.txt","a") as op:
                op.write(str([str(getime())])+":"+ value + "\n")
                print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("rohan-ex.txt","a") as op:
                op.write(str([str(gettime())])+ ":"+value + "\n")
                print("successfully written")
        elif (c==2):
            value = input ("type here \n")
            with open("rohan-food.txt","a") as op:
                op.write(str([str(gettime())])+ ":" + value + "\n")
                print("successfully written \n")
    elif (k==3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c==1):
            value = input("type here \n")
            with open ("sohan-ex.txt","a") as op:
                op.write(str([str(gettime())])+ ":" + value + "\n")
                print("successfully written \n")
        elif (c==2):
            value = input("type here \n")
            with open ("soha-food.txt","a") as op:
                op.write(str([str(gettime())])+ ":" + value + "\n")
                print("successfully written \n")
    else:
        print("please enter valid input (1(harry)),(1(rohan)),(3(sohan))")
def retrieve(k):
    if (k==1):
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif (c==2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif (k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c==1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif (k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("sohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("sohan-food.txt") as op:
                for i in op:
                    print(i,end="")

    else:
        print("please enter valid input (1(harry)),(1(rohan)),(3(sohan))")

print("health management system:")
a = int(input("press 1 for lock the value and 2 for retrieve"))

if a==1:
    b = int(input("press 1 for harry , b for rohan, c for sohan" ))
    take(b)
else:
    b = int(input("press 1 for harry , b for rohan, c for sohan"))
retrieve(b)
        
                

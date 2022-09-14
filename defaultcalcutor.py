print("Enter your first numner")
a = int(input())
print(" Enter second number")
b = int(input())
print = ("which operator you want to perform?",
         "+"   ,
         "-"  ,
         "*"   ,
         "/" )
operator=("enter your choice")
print(input(operator()))
if  a==45 & b==3 & operator=="*":
    print("555")
elif a==56 & b== 6 & operator=="+":
    print("77")
elif a==56 & b== 6 & operator== "/":
    print("4")

elif operator== "+":
    sum = a+b
    print(sum)
elif operator == "-":
    sub = a-b
    print(sub)
elif operator == "*":
    num = a*b
    print(num)
elif operator == "/":
    div = a/b
    print(div)

a = int(input("please input the first number "))
b = int(input("please input the second number "))
gcd = 1
def min(a,b):
    if a>b:
        smaller = a
    else :
        smaller = b

def get_GCD(a,b):
    s=min(a,b)
    for i in range(s,0,-1):
        if a%i==0 and b%i==0:
            gcd=i
            break
        return gcd
print("the GCD of",a,"and",b,"is",get_GCD(a,b))

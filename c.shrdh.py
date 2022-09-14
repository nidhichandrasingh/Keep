c=0
def generatenext(d,num):
       global c
       c = c + d
       return num
       
c = float(input("please input the string for yor series"))
s= float(input("please input the d for your series"))
print ("the series produced by this method is")
for i in range (1,11):
    print(generatenext(s,c),end=",")
    

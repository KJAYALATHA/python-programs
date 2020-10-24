n1=int(input("enter the number "))
n2=int(input("enter the number "))
lcm=1
for i in range(1,n2,1):
    if(n1%i==0)or(n2%i==0):
        lcm=1*i
print(lcm)    
        

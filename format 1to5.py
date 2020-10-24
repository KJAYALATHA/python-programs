n=int(input("enter the number:"))
sum=0
for i in range(n+1):
    for j in range(i):
        sum=sum+1
        print(sum,end=" ")
    print()
    
    

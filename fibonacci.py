m=[]
n=int(input("enter a number"))
n1=0
n2=1
for i in range(n):
    if(i==0)or(i==1):
        m.append(i)
    else:
        result=n1+n2
        n1=n2
        n2=result
        m.append(result)
print(m)
    

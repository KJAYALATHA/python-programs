m=[]
n=int(input("enter the no:"))
for i in range(n):
        x=(int(input("enter the number to sort:")))
        m.append(x)
for i in range(n):
    for j in range(n-1):
        if(m[j]>m[j+1]):
            a=m[j]
            m[j]=m[j+1]
            m[j+1]=a
print(m)
    

        

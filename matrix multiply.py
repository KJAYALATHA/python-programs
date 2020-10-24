m1=[]
m2=[]
result=[]
for k in range(1,3):
    print("enter",k,"matrix")
    m=int(input("enter  rows:"))
    n=int(input("enter  colum:"))
    for i in range(m):
        a=[]
        for j in range(n):
            a.append(int(input("enter a matrix "))) 
        if(k==1):
            m1.append(a)
        elif(k==2):
            m2.append(a)
for i in range(m):
    result.append([])
    for j in range(n):
        z=0
        result[i].append(z)
print(result)
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            result[i][j]+=m1[i][k]*m2[k][j]
print("result matrix is :")
for i in range(m):
    for j in range(n):
        print((result[i][j]),end=" ")
    print()




        

       

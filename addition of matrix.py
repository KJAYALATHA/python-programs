m1=[]
m2=[]
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
print("1st matrix is :")
for i in range(m):
    for j in range(n):
        print((m1[i][j]),end=" ")
    print()
print("2nd matrix is :")
for i in range(m):
    for j in range(n):
        print((m2[i][j]),end=" ")
    print()
result=[[0,0],[0,0]]
for i in range(len(m1)):
    for j in range(len(m2)):
            result[i][j]=m1[i][j]+m2[i][j]
print("result matrix is :")
for i in range(m):
    for j in range(n):
        print((result[i][j]),end=" ")
    print()




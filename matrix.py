n=int(input("enter a matrix:"))
m=[]
m1=[]
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(int(input("enter 1 matrix ")))

for i in range(n):
    for j in range(n):
        m1.append(int(input("enter 2 matrix ")))
print(m1)
for i in range(n):
    for j in range(n):
        print(m[i][j],end=" ")
        print
    print()


        

      

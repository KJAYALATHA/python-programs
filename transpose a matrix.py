m=[]
m1=[]
n=int(input("enter a matrix :"))
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(int(input("enter a numbers :")))
for i in range(n):
    m1.append([])
    for j in range(n):
        z=0
        m1[i].append(z)
print("the transpose of matrix")
for i in range(n):
    for j in range(n):
        m1[i][j]+=m[j][i]
        print(m1[i][j],end=" ")
    print()


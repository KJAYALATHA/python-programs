m=[]
n=int(input("enter a matrix :"))
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(int(input("enter a numbers :")))
for i in range(n):
    sum=0
    for j in range(n):
        sum=sum+m[i][j]
    print("the row sum",sum)
print()
for i in range(n):
    sum=0
    for j in range(n):
        sum=sum+m[j][i]
    print("the column sum",sum)
print()




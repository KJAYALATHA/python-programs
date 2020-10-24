m=[]
row=int(input("enter a row :"))
col=int(input("enter a column:"))
for i in range(row):
    m.append([])
    for j in range(col):
        m[i].append(int(input("enter a numbers :")))
for i in range(row):
    for j in range(col):
        print(m[i][j],end="")
    print()
'''for i in m[0]:
    temp=i
    break
for i in range(1,3):
    tl=m[i]
    for j in range(len(tl)):
        if j<3:
             tl[j]=tl[j+1]
        else:
             tl[j]=temp
print(m[0])
for i in range(1):
        m1=m[0]
        m2=m[1]
        m3=m[2]
        m4=m[3]
        m1[3]=m2[3]
        m2[3]=m3[3]
        m3[3]=m4[3]
        m4[3]=temp
print(m)
for i in (m[3]):
    temp=i
for i in range(1):
    tl=m[3]
    print(tl)
    for j in range(1,5):
        print(tl[-j])
        if j<4:
            tl[-j]=tl[-j-1]
        else:
            tl[-j]=temp
print(m[3])
for i in (m[3]):
    temp=i
    break
for i in range(1):
    r2=m[1]
    r3=m[2]
    r4=m[3]
    r4[0]=r3[0]
    r3[0]=r2[0]
    r2[0]=temp
print("swapped first column",m)
for i in range(1):
    r2=m[1]
    r3=m[2]
    for i in range(1,3):
        if i==1:
            temp=r2[i]
            r2[i]=r3[i+1]
            r3[i+1]=temp
        else:
            temp=r2[i]
            r2[i]=r3[i-1]
        r3[i-1]=temp
            
print("rotated matrix",m)'''

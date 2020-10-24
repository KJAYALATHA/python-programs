m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(m)
for i in range(2):
    #for first row
    for i in (m[0]):
        temp=i
        break

    for i in range(1):
        tl=m[i]
        for j in range(len(tl)):
            if j<3:
                tl[j]=tl[j+1]
            else:
                tl[j]=temp
    print("now the swapped 1st row is:",m[0])


    #for last column
    for i in (m[0]):
        temp=i

    for i in range(1):
        m1=m[0]
        m2=m[1]
        m3=m[2]
        m4=m[3]
        m1[3]=m2[3]
        m2[3]=m3[3]
        m3[3]=m4[3]
        m4[3]=temp
    print("swapped last elemetns(last column)",m)

    #for last row
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
    print("now the swapped last row is:",m[3])
 #for first column
for i in (m[3]):
        temp=i
        break
for i in range(1):
    r2=m[1]
    r3=m[2]
    r4=m[3]
    r4[0]=r3[0]
    r3[0]=r2[0]
    sr2[0]=temp
    print("swapped first column",m)
#inner matrix
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
            
print("rotated matrix",m)

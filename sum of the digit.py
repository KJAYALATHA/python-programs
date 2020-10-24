n=int(input("sum of the digit is :"))
sum=0
while n>0:
    rem=n%10
    n=n//10
    sum=sum+rem
print(sum)
   


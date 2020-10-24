n=int(input("sum of the digit is :"))
b=n
a=0
while n>0:
    n1=n%10
    a=a*10+n1
    n=n//10
print("the reversed int",a)
if(b==a):
    print("palindrome")
else:
    print("not palindrome")

   

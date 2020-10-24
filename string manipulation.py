n=(input("enter a word:"))
a=0
d=0
v=0
c=0
for i in n:
    if (i.isalpha()):
        a=a+1
    elif (i.isdigit()):
        d=d+1
    if i in 'aeiouAEIOU':
        v=v+1
    elif i.isalpha():
        c=c+1
print(a,d,v,c)
search=(input("enter a search word: "))
replace=(input("enter a replace word: "))
if n.find(search):
    n=n.replace(search,replace)
    print("text found and replace",n)
else:
    print("not found")


 

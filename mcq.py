str1=""
i=0
var2=1
while(i<3):
    var1=1
    if str1:
        var2=var1*var2+5
    else:
        var2=var1*var2+1
    i=i+1
print(var2)


str = input("enter string- ")
rstr = ""
n = len(str)

for i in range(n):
    rstr+= str[(n-1)]
    n=n-1
print(rstr)

if str==rstr:
    print("pali")
else:
    print("not")
n=input("array= ")
li=n.split(",")
print(li)
s=sorted(li)
print(s)
s1=len(s)
if (s1%2==0):
    print(s[(s1//2)-1],s[s1//2])
else:
    print(s[s1//2])
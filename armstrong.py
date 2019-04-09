import math
n=int(input())
s1=0
m=n
while(n>0):
    s= math.pow((n%10),3)
    s1=s1+s
    n=n//10
if m==s1:
    print('yes')
else:
    print('no')
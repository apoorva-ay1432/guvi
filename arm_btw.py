import math
n=int(input('1st: '))
m=int(input('2nd: '))

for num in range(n,m):
    s1=0
    # o=len(str(num))
    i=num
    while(i>0):
        s=i%10
        s1+=s**3
        i=i//10
    if num==s1 :
        print(s1)
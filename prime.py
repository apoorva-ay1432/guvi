import math
n=int(input())
f=0
for i in range(2,int(n)):
    if(n%i)==0:
        print("not prime")
        break
    else:
        print("prime")
        break
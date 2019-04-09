import math
n=int(input('1st : '))
m=int(input("2nd : "))
for i in range(n,m):
    if i>1:
        for num in range(2,i):
            if(i % num)==0:
                break
        else:
            print(i)
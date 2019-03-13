n=int(input())
count=0
while (n>0):
    n=n//10
    count+=1
    n+=1
print(count)
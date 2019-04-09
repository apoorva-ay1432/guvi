n1=int(input('enter number'))
n2=int(input('enter number'))
li=[]
sum1=0
for i in range(1,n1):
    li.append(i)
for j in range(0,n2):
    sum1=sum1+li[j]
# print(li)
# print(sum1)
print(li,'\n',sum1)
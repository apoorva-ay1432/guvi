n=input()
# li=[]
# list(str(n))
# li=map(int,str(n))
lr=[]
li=[int(i) for i in str(n)]
for i in reversed(li):
    lr+=[i]
if li==lr:
    print('Palindrome')
else:
    print('Not palindrome')
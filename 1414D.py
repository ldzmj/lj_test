s=0
n=int(input())
for i in range(1,n+1):
    if i%2==0:continue
    else:
        s+=i
print(s)
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input('Enter the Value: '))
sum=0
num=n
while num>0:
    d=num%10
    sum=sum+fact(d)
    num=num//10
if sum==n:
    print('It is Strong No')
else:
    print('It is not Strong No')


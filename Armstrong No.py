n=int(input('Enter the Number: '))
num=n
sum=0
while(num>0):
    d=num%10
    sum=sum+(d*d*d)
    num=num//10
if(sum==n):
    print('It is Armstrong No')
else:
    print('It is not Armstrong No')

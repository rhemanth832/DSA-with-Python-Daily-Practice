n=int(input('Enter the number: '))
num=n
sum=0
while (num > 0):
    d=num%10
    sum=(sum*10)+d
    num=num//10
print("The Reverse of a No is ", sum)
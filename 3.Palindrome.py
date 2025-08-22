n=int(input('Enter the number: '))
num=n
sum=0
while (num > 0):
    d=num%10
    sum=(sum*10)+d
    num=num//10
if(sum==n):
    print("The number is Palindrome")
else:
    print("The no is not palindrome")

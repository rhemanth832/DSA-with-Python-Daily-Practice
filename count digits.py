n=int(input('Enter the number: '))
num=n
sum=0
while (num > 0):
    last_digit=num%10 # retriving last digit, remainder
    sum=sum+1
    num=num//10 # removing last digit
print(sum)

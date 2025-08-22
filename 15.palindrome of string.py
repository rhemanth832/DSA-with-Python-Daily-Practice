s=int(input('Enter a String: '))
is_palindrome= True
left=0
right=len(s)-1
while left <right:
    if s[left]!=s[right]:
        is_palindrome=False
        break
        left += 1
        right-=1
if is_palindrome:
    print('Palindrome')
else:
    print('Not Palindrome')

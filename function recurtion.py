def func(sum,i,N):
    if i>N:
        print(sum)
        return
    func(sum+i,i+1,N)
N = int(input("Enter the Value: "))
func(0, 1, N)

#Recurtion
def func(N):
    if N==1:
        return 1
    return N+func(N-1) # 4+3+2+1=10
N=int(input('Enter the Value: '))
print(func(N))
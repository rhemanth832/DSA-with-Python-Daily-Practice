#print value N number of times
def func(X,N):
    #global N
    #global X
    if N==0:
        return
    print(X)
    func(X,N-1)
func(15,4)

#print 1 to N numbers
def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
func(1,4)
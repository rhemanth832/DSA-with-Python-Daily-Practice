count=0
def func():
    global count
    if count==4:
        return
    print('Anirudh')
    count+=1
    func()
func()

class Minstack(object):
    def __init__(self):
        self.stack=[]
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        if self.stack:
            self.stack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
    def getMin(self):
        return min(self.stack) if self.stack else None
ms = Minstack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.getMin())   # -3
ms.pop()
print(ms.top())      # 0
print(ms.getMin())   # -2



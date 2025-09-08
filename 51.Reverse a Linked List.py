from collections import deque
dq=deque()
dq.append(5)
dq.append(10)
dq.append(15)
dq.append(20)
dq.reverse()
print("->".join(map(str, dq))+"->None")
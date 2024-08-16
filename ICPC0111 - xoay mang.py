import queue 
t = int(input())

for i in range(t):
    n,k = map(int,input().split())
    lst = [x for x in input().split()]
    q = queue.Queue()
    for x in lst:
        q.put(x)
    while k:
        a = q.get()
        q.put(a)
        k-=1
    b = 0
    while not q.empty():
        x = q.get()
        lst[b] = x
        b+=1
    for x in lst:
        print(x, end = ' ')
    print()
        
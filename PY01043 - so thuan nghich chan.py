from collections import deque

def main():
    t = int(input())
    q = deque()
    a = ['0','2','4','6','8']
    for i in a:
        if i != '0':
            q.append(i)
    tn =[]
    while(len(q)):
        s = q.popleft()
        x = s + s[::-1]
        if(int(x)>10):
            tn.append(x)
        for i in a:
            b = s+i
            if(len(b)<4):
                q.append(b)
    for _ in range(t):
        n = int(input())
        for i in tn:
            if int(i) < n:
                print(i,end=' ')
            else:
                break
        print()
if __name__=="__main__":
    main()
        
        
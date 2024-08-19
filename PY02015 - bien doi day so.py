def main():
    from math import fabs
    while True:
        s = list(map(int,input().split()))
        if sum(1 for x in s if x == 0) == 4:
            return
        a = s[0]
        cnt = 0
        while sum(1 for x in s if x!=a):
            for i in range(4):
                if i == 3:
                    s[3] = fabs(s[3]- a)
                else:
                    s[i] = fabs(s[i]-s[i+1])
            
            cnt +=1
            a = s[0]
        print(cnt)
if __name__ == "__main__":
    main()

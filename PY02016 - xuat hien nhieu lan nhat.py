def main():
    for _ in range(int(input())):
        n = int(input())
        s = list(map(int,input().split()))
        m =dict()
        ok = False
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i]+=1
            if(m[i]>n/2):
                print(i)
                ok = not ok
                break
        if not ok:
            print('NO')
if __name__ =="__main__":
    main()
        
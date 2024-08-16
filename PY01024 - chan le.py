def main():
    t = int(input())
    for i in range(t):
        s = list(input())
        s = list(map(int,s))
        if sum(s) % 10 !=0 :
            print('NO')
            continue
        if any(i for i in range(len(s)-1) if abs(s[i]-s[i+1]) != 2):
            print('NO')
            continue
        print('YES')

if __name__ =="__main__":
    main()
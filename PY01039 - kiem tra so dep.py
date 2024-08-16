def main():
    t = int(input())
    for _ in range(t):
        x = input()
        if len(set(x))!=2:
            print('NO')
            continue
        if any(x[i] for i in range(0,len(x),2) if x[i] != x[0]):
            print('NO')
            continue
        if any(x[i] for i in range(1,len(x),2) if x[i]!=x[1]):
            print('NO')
            continue
        print('YES')

if __name__ =="__main__":
    main()
def main():
    for _ in range(int(input())):
        input()
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        a = sorted(a)
        b = sorted(b)
        ok = True
        for i in range (len(a)):
            if(a[i] > b[i]):
                ok = False
                break
        if not ok:
            print('NO')
        else:
            print('YES')

if __name__ == "__main__":
    main()
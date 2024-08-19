def main():
    input()
    a = list(map(int,input().split()))
    ok = True
    cnt = 0
    if a[0] == 0:
        ok = False
    for i in range(1,len(a)):
        if not ok and a[i] == 1:
            cnt +=1
            ok = not ok
        elif ok and a[i] == 0:
            cnt +=1
            ok = not ok
    print(cnt)

if __name__ == "__main__":
    main()
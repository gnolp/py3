def main():
    t = int(input())
    for _ in range(t):
        cnt = 1000
        n = int(input())
        ok = False
        while cnt > 0:
            if(n%7==0):
                print(n)
                ok = True
                break
            n += int(str(n)[::-1])
            cnt -=1
        if not ok:
            print(-1)
if __name__ == "__main__":
    main()
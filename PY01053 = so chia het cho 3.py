def main():
    t = int(input())
    for _ in range(t):
        s = input()
        n = sum(int(i) for i in list(s))
        if n%3==0:
            print('YES')
        else:
            print('NO')

if __name__ =="__main__":
    main()
def main():
    t = int(input())
    for _ in range(t):
        s = input()
        if not s.isdigit():
            print('NO')
            continue
        if any(x for x in s if int(x) not in[0,1,2]):
            print('NO')
        else:
            print('YES')

if __name__ =="__main__":
    main()
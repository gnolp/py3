def main():
    t = int(input())
    for i in range (t):
        s = input()
        if(s[-2:]=='86'):
            print('YES')
        else:
            print('NO')

if __name__ =="__main__":
    main()
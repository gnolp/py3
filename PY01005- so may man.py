def main():
    t = int(input())
    for i in range(t):
        n = input()
        a = n.count('4')
        b = n.count('7')
        if a + b != len(n):
            print('NO')
        else:
            print('YES')
if __name__ =="__main__":
    main()
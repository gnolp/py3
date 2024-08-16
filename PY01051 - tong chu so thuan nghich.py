def main():
    for _ in range(int(input())):
        s = input()
        s = sum(int(i) for i in s)
        if len(str(s)) > 1 and s == int(str(s)[::-1]):
            print('YES')
        else:
            print('NO')

if __name__ =="__main__":
    main() 
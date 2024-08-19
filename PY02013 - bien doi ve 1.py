def main():
    while True:
        n = int(input())
        if n == 0:
            break
        s = set()
        
        if n == 1:
            print(1)
        else:
            s.add(n)
            while(n!=1):
                if n % 2 == 1:
                    n = n*3+1
                    s.add(n)
                else:
                    n /=2
                    s.add(n)
            print(len(s))

if __name__ == "__main__":
    main()
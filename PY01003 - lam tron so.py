def main():
    t = int(input())
    for i in range(t):
        n = input()
        s = len(n)
        n = int(n)
        if(n<=10):
            print(n)
        else:
            while n > 10:
                if(n%10 == 5):
                    n /= 10
                    n = round(n + 1e-9)
                else:
                    n/=10
                    n = round(n)   
            print(n*(10**(s-1)))
if __name__ =="__main__":
    main()

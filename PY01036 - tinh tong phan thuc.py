def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n%2 ==0:
            ans = sum(1/x for x in range(2,n+1,2))
        else:
            ans = sum(1/x for x in range(1,n+1,2))
        print(f"{ans:.6f}")
if __name__ == "__main__":
    main()
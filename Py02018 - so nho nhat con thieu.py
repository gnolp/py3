def main():
    input()
    a = list(map(int,input().split()))
    a.sort()
    x = a[0]
    for i in range(1,len(a)):
        if a[i]!=x+1:
            print(x+1)
            return
        x+=1
    if x == a[-1]:
        print(x+1)

if __name__ == "__main__":
    main()
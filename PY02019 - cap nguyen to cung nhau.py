def main():
    input()
    a = list(map(int, input().split()))
    a.sort()
    from math import gcd
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if gcd(a[i],a[j])==1:
                print(f"{a[i]} {a[j]}")

if __name__ =="__main__":
    main()
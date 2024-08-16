from math import gcd
def main():
    l,r = [int(x) for x in input().split()]
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            if gcd(i,j) == 1:
                for k in range(j+1,r+1):
                    if gcd(k,i) == 1 and gcd(k,j) == 1:
                        print(f"({i}, {j}, {k})")

if __name__ =="__main__":
    main()
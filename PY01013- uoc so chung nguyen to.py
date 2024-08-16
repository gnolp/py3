from math import isqrt, gcd

def nto(n:int)-> bool:
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i ==0:
            return False
    return True
def main():
    t = int(input())
    for i in range(t):
        a,b = [int(x) for x in input().split()]
        c = gcd(a,b)
        x = sum(int(i) for i in str(c))
        if nto(x):
            print("YES")
        else:
            print("NO")
if __name__ =="__main__":
    main()
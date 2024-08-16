from math import isqrt
def nto(n:int)-> bool:
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True
def main():
    t = int(input())
    for _ in range(t):
        s = input()
        if not nto(len(s)):
            print('NO')
            continue
        nto_count = sum(1 for x in s if x in ['2','3','5','7'])
        if nto_count > len(s) - nto_count:
            print("YES")
            continue
        print("NO")
if __name__ =="__main__":
    main()
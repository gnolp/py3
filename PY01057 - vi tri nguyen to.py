from math import isqrt

def nto(n: int)-> bool:
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i==0:
            return False
    return True

def main():
    for _ in range(int(input())):
        s = input()
        if (any(i for i in range(len(s)) if nto(i) and s[i] not in ['2','3','5','7'])) or (any(i for i in range(len(s)) if not nto(i) and s[i] in ['2','3','5','7'])):
            print('NO')
            continue
        print('YES')
if __name__ =="__main__":
    main()
def nto(n:int)->bool:
    if n<2:
        return False
    from math import isqrt
    for i in range(2,isqrt(n)+1):
        if n%i == 0:
            return False
    return True

def main():
    for _ in range(int(input())):
        s = input()
        s = s[-4:len(s)+1]
        if nto(int(s)):
            print('YES')
        else:
            print('NO')
if __name__ =="__main__":
    main()
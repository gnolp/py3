from math import isqrt
def nto(n:int)->bool:
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i ==0:
            return False
    return True

def main():
    for _ in range(int(input())):
        s = input()
        x = sum(1 for i in s if i in ['2','3','5','7'])
        if nto(len(s)) and x > len(s)-x:
            print('YES')
        else:
            print('NO')

if __name__ =="__main__":
    main()
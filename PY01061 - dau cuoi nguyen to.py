from math import isqrt
def nto(n:int)->bool:
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

def main():
    for _ in range(int(input())):
        s = input()
        
        if nto(int(s[:3])) and nto(int(s[-3:len(s)+1])):
            print('YES')
        else:
            print('NO')

if __name__ == "__main__":
    main()
import math
def nto(n :int) -> bool:
    if n<2:
        return False
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        cnt = 0
        for j in range(n):
            if math.gcd(n,j)==1:
                cnt +=1
        if(nto(cnt)):
            print('YES')
        else:
            print('NO')
if __name__ == '__main__':
    main()
from math import gcd
def main():
    t = int(input())
    for i in range(t):
        s = input()
        y = s[::-1]
        if(gcd(int(s),int(y)) == 1 ):
            print('YES')
        else:
            print('NO')
if __name__ =='__main__':
    main()

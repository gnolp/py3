def main():
    n,m = [int(x) for x in input().split()]
    a = [[0]*m for _ in range(n)]
    def nto(n:int)->bool:
        if n< 2:
            return False
        from math import isqrt
        for i in range(2,isqrt(n)+1):
            if(n%i) ==0:
                return False
        return True
    for i in range(n):
        x = input().split()
        for j in range(m):
            a[i][j] = int(x[j])
            if nto(a[i][j]):
                a[i][j] =1
            else:
                a[i][j] = 0
    for i in range(n):
        for j in range(m):
            print(a[i][j],end =' ')
        print()
if __name__ =="__main__":
    main()
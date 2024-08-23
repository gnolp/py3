from math import *
def main():
    n = int(input())
    a = [[0]*n for _ in range(n)]
    st = 0
    for i in range(n):
        x = input().split()
        for j in range(n):
            a[i][j] = int(x[j])
            if j!=(n-i-1):
                st += int(x[j])
    so = 0
    for i in range(n):
        for j in range(n-i-1):
            so += a[i][j]
    
    k = int(input())
    chenhlech = abs(so-(st-so))
    if(k >= chenhlech):
        print('YES')
    else:
        print("NO")
    print(chenhlech)

if __name__ =="__main__":
    main()

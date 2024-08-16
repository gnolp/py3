from math import isqrt
from bisect import bisect_left

def main():
    a = [0] * 10000001  
    
    for i in range(1, 10000001):
        for j in range(1, isqrt(i) + 1):
            if i % j == 0:
                if j == i // j:
                    a[i] += 1  
                else:
                    a[i] += 2  
    
    pt = []
    m = 0  
    for i in range(1, len(a)):
        if a[i] > m:
            pt.append(i)
            m = a[i]
    t = int(input())
    for _ in range(t):
        x = int(input())
        y = bisect_left(pt, x)
        print(pt[y])

if __name__ == "__main__":
    main()

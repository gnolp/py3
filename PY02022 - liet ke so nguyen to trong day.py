import math
def nto(n) :
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def main():
    m = {}
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in a:
        if nto(i) == 1:
            if i in m:
                m[i] += 1
            else :
                m[i] = 1
    for i in m:
        print(i, m[i])
if __name__ =="__main__":
    main()

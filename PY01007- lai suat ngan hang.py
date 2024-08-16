import math

def main():
    t = int(input())
    for i in range(t):
        n,x,m = [float(x) for x in input().split()]
        s = math.log(m/n,1+x/100)
        if s != int(s) : s = s + 1
        print(int(s))
if __name__ =="__main__":
    main()
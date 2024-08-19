def main():
    import sys
    input = sys.stdin().read()
    s = list(map(int,input().split()))
    a = [0]*42
    for i in s:
        a[i%42] +=1
    print(sum(1 for x in a))

if __name__ =="__main__":
    main()

def main():
    n,k = [int(x) for x in input().split()]
    a = list(map(int, input().split()))
    a = list(set(a))
    import itertools
    a = sorted(a)
    
    ckn = list(itertools.combinations(a,k))
    for i in ckn:
        x = list(i)
        print(' '.join(list(map(str,x))))
if __name__ =="__main__":
    main()
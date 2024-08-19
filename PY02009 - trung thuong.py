def main():
    for _ in range(int(input())):
        n = int(input())
        d = dict()
        for _ in range(n):
            x = int(input())
            if x not in d:
                d[x] = 1
            else:
                d[x] +=1
        d = sorted(d, key =lambda x: [~d[x],x])
        print(d[0])
if __name__ =="__main__":
    main()
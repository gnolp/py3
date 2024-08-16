def main():
    n = int(input())
    a = list(map(int, input().split()))
    na = []
    for i in a:
        if(len(na) > 0):
            if (na[len(na)-1] + i) %2 == 0:
                na.pop()
            else:
                na.append(i)
        else:
            na.append(i)
    print(len(na))

if __name__ =="__main__":
    main()
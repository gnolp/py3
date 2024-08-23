def main():
    for _ in range(int(input())):
        input()
        a = input().split()
        def cs(s:str)->int:
            ans = 1 
            for i in s:
                ans *= int(i)
            return ans
        b = [cs(x) for x in a]
        c = list(zip(a,b))
        c = sorted(c, key= lambda x: [x[1],int(x[0])])
        for i in c:
            print(i[0], end=' ')
        print()

if __name__ =="__main__":
    main()
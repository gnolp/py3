f = [1] * 93

for i in range(3,len(f)):
    f[i] = f[i-1] + f[i-2]
def main():
    for _ in range(int(input())):
        l,r = [int(x) for x in input().split()]
        for i in range(l,r+1):
            print(f[i],end = ' ')
        print()
if __name__ =="__main__":
    main()
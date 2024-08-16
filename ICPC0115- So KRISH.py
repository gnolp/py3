
a =[1,1,2,6,24,120,720,5040,40320,362880]
def check(n:str) ->int:
    ans = 0
    for i in n:
        ans += a[int(i)]
    return ans

def main():
    t = int(input())
    for i in range(t):
        n = input()
        if check(n) == int(n) :
            print('Yes')
        else:
            print('No')

if __name__ =="__main__":
    main()


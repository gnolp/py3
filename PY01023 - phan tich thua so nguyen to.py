def main():
    t = int(input())
    for i in range (t):
        n = int(input())
        print('1 ',end = '')
        cnt = 0
        for j in range (2,n+1):
            while n%j ==0:
                n = n//j
                cnt +=1
            if(cnt != 0):
                print(f"* {j}^{cnt} ", end='')
                cnt = 0

        print()
if __name__=="__main__":
    main()

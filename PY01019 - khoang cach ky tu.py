def main():
    t = int(input())
    for i in range(t):
        s = input()
        l,r = 1,len(s)-2
        ok = True
        while(l<=r):
            if abs(ord(s[l])-ord(s[l-1])) != abs(ord(s[r]) - ord(s[r+1])):
                
                ok = False
                break
            l +=1
            r -=1
        if not ok:
            print('NO')
        else:
            print('YES')

if __name__ == "__main__":
    main()
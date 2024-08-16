def main():
    t = int(input())
    for i in range(t):
        s = input()
        c = s[0]
        j = 0
        cnt = 0
        ans =''
        while j<len(s):
            if s[j] == c:
                cnt +=1
            else:
                ans = ans + str(cnt) + c
                c = s[j]
                cnt = 1
            j += 1
        ans = ans + str(cnt) + c
        print(ans)
if __name__ =="__main__":
    main()
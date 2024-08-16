def main():
    t = int(input())
    for i in range(t):
        s = input()
        x = ''
        for i in range(0,len(s)-1,2):
            x += s[i]*int(s[i+1])
        print(x)
if __name__ =="__main__":
    main()
def main():
    for _ in range(int(input())):
        s = input()
        chan = sum(int(s[i]) for i in range(0,len(s),2))
        print(chan,end = ' ')
        ok = True
        le = 1
        for i in range(1,len(s),2):
            if(s[i]!= '0'):
                le*= int(s[i])
                ok = False
        if not ok:
            print(le)
        else:
            print(0)
if __name__ =="__main__":
    main()
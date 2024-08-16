def main():
    P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    while True:
        a = input().split()
        k = int(a[0])
        if k ==0 :
            break
        s = list(a[1])
        for i in range(len(s)):
            s[i] = P[(P.find(s[i])+k)%28]
        print(''.join(s)[::-1])
if __name__ =="__main__":
    main()
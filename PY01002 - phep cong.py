def main():
    s = input()
    a,b,c = int(s[0]), int(s[4]),int(s[8])
    d = s[2]
    if(d =='+'):
        if a + b == c:
            print('YES')
            return
    elif(d=='-'):
        if a - b == c:
            print('YES')
            return
    elif(d=='*'):
        if a*b == c:
            print('YES')
            return
    elif(d=='/'):
        if a/b == c:
            print('YES')
            return
    print('NO')
    return
if __name__ =="__main__":
    main()
def main():
    t = int(input())
    for i in range(t):
        x = input()
        
        if x[:2] == x[-2:]:
            print('YES')
            
        else:
            print('NO')
if __name__ =="__main__":
    main()
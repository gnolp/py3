def main():
    for _ in range(int(input())):
        s = input()
        from math import prod
        s = prod(int(x) for x in s if x != '0')
        print(s)

if __name__ =="__main__":
    main()
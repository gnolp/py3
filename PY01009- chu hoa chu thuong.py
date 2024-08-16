def main():
    s = input()
    ch = sum(1 for x in s if x.isupper())
    ct = len(s) - ch
    if ct >= ch:
        print(s.lower())
    else:
        print(s.upper())

if __name__ =="__main__":
    main()
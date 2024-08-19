def main():
    s = input()
    import  itertools
    p = list(itertools.permutations(s))
    for i in p:
        print(''.join(i))

if __name__ =="__main__":
    main()
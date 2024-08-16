def main():
    t = int(input())
    m ={
    }
    for i in range(t):
        s= input()
        if s not in m:
            m[s] = 1
        else:
            m[s] +=1
    print(len(m))
if __name__ =="__main__":
    main()
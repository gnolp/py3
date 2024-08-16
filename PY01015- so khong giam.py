def check(x:str)-> bool:
    for i in range(len(x)-1):
        if(int(x[i])>int(x[i+1])):
            return False
    return True

def main():
    t = int(input())
    for i in range(t):
        x = input()
        if check(x) :
            print("YES")
        else:
            print("NO")

if __name__ =="__main__":
    main()
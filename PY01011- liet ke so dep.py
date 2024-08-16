
def check(x : str) -> bool:
    if x!= x[::-1]:
        return False
    if(int(x) < 10):
        return False
    if any(i in x for i in ['1','3','5','7','9']):
        return False
    
    if len(x) % 2 != 0:
        return False
    return True
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        for x in range(n):
            if check(str(x)):
                print(x,end= ' ')
        print()
if __name__ == "__main__":
    main()
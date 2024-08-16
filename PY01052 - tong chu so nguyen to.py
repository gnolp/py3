def main():
    def nto(s:int)->bool:
        if s < 2:
            return False
        from math import isqrt
        for i in range(2,isqrt(s)+1):
            if(s%i==0):
                return False
        return True
    for _ in range(int(input())):
        s = input()
        s = sum(int(i) for i in s)
        if not nto(s):
            print('NO')
        else: print('YES')
        
if __name__ =="__main__":
    main()
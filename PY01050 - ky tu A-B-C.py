a = ['A','B','C']
def main():
    n = int(input())
    result = []
    def Try(n,s):
        for i in a:
            b = s + i
            if(n>=1):
                if check(b):
                    result.append(b)
                Try(n-1,b)
    def check(s:str)->bool:
        if 'C' not in s or 'A' not in s or 'B' not in s:
            return False
        if s.count('A') > s.count('B') or s.count('B') > s.count('C'):
            return False
        return True
    Try(n,"")
    result = sorted(result, key = lambda x: [len(x),x])
    for x in result:
        print(x)
if __name__ =="__main__":
    main()

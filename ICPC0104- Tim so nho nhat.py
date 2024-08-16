import re

def main():
    t = int(input())
    for i in range(t):
        s = input()
        pattern = '\\d+'
        result = list(map(int,re.findall(pattern,s)))
        print(min(result))
if __name__ =="__main__":
    main()
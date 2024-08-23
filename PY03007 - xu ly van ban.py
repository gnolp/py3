import re
import sys

def main():
    pattern = '[.!?]'
    s = sys.stdin.read()
    sentences = re.split(pattern, s)
    for i in sentences:
        x = i.strip().lower().split()
        if(x!=[]):
            x[0] = x[0].capitalize()
        print(' '.join(x))
if __name__ == "__main__":
    main()

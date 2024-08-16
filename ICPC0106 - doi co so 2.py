'''long'''
test = int(input())

for i in range (test):
    hs = int(input())
    s = input()
    if(hs == 2):
        print(s)
    elif hs == 4:
        if(len(s)%2 ==1):
            s = '0' + s
        temp =""
        for i in range (0,len(s),2):
            t = 0
            if(s[i]=='1'):
                t += 2
            if s[i+1]=='1':
                t += 1
            temp += str(t)
        print(temp)
    elif hs == 8:
        if(len(s)%3 !=0):
            for i in range (0,3-len(s)%3):
                s = '0' + s
        temp =""
        for i in range (0,len(s),3):
            t = 0
            if(s[i]=='1'):
                t += 4
            if s[i+1]=='1':
                t += 2
            if s[i+2] == '1':
                t += 1
            temp += str(t)
        print(temp)
    elif hs == 16:
        if(len(s)%4 !=0):
            for i in range (0,4-len(s)%4):
                s = '0' + s
        temp =""
        for i in range (0,len(s),4):
            t = 0
            if(s[i]=='1'):
                t += 8
            if s[i+1]=='1':
                t += 4
            if s[i+2] == '1':
                t += 2
            if s[i+3] == '1':
                t += 1
            if t >= 10:
                a = 65
                a += t-10
                temp += chr(a)
            else :
                temp += str(t)
        print(temp)

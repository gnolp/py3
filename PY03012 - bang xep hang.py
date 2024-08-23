
def main():
    sv ={

    }
    for _ in range(int(input())):
        name = input()
        ac,sub = [int(x) for x in input().split()]
        sv[name] = (ac,sub)

    sorted_sv = sorted(sv.items(), key=lambda x: (-x[1][0], x[1][1], x[0]))
    for i in sorted_sv:
        print(f"{i[0]} {i[1][0]} {i[1][1]}")
        
if __name__ =="__main__":
    main()
def main():
    T=int(input())
    while T>0:
        N= int(input())
        A=[int(x) for x in input().strip().split()]
        for i in A[::-1]:
           print(i, end = " ")
        print()
        T-=1
        
if __name__ == "__main__":
   main()
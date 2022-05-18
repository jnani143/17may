t=int(input())
while t:
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    pf=[0]*n
    pf[0]=arr[0]
    if n<2:
        print("1")
    else:
        for i in range(1,n):
            pf[i]=pf[i-1]+arr[i]
        for i in range(n):
            if i==0:
                lsum=0
            else:
                lsum=pf[i-1]
            rsum=pf[n-1]-pf[i]
            if lsum==rsum:
                print(i+1)
            else:
                print(-1)

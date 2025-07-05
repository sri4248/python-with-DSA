a=list(map(int,input().split()))
n=len(a)
if n<2:
    print(0)
else:
    a.sort()
    max_gap=0
    for i in range(1,n):
        gap=a[i]-a[i-1]
        if gap>max_gap:
            max_gap=gap
    print(max_gap)
        

def maxerase(a,n,k):
    maxsum=s=sum(s[:k])
    for i in range(k-1):
        s=s-a[k-i-1]+a[n-1-i]
        maxsum=max(maxsum,s)
    return maxsum
n,k=map(int,input().split())
a=list(map(int,input().split()))
print(maxerase(a,n,k))

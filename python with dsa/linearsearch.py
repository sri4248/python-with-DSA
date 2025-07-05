#//linear search
def linearsearch(a,n,k):
    for i in range(n):
        if a[i]==k:
            return i
    return -1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(linearsearch(a,n,k))
       

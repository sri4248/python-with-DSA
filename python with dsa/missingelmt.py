#to find missing element from the given element
n=int(input())
a=list(map(int,input().split()))
s1=n*(n+1)//2
s2=sum(a)
print(s1-s2)

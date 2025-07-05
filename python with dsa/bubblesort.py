my_arr=[64,34,25,12,22,11,90,5]
n=len(my_arr)
for i in range(n-1):
    for j in range(n-i-1):
        if my_arr[j]>my_arr[j+1]:
            my_arr[j],my_arr[j+1]=my_arr[j+1],my_arr[j]

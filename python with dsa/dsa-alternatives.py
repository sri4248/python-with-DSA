# Iterate Python Program to print alternate elements
# of the array

def printAlternates(arr):
    for i in range(0, len(arr), 2):
        print(arr[i], end=" ")

# Example
arr = [10, 20, 30, 40, 50]
printAlternates(arr)


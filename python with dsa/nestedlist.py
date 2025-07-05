l1=[10,20,30,40,23,56,78,-10]
print(max(l1))
print(min(l1))
print(20 in l1)
print(56 not in l1)
#nested list
l2=[[10,20,30],[1,2,3],[1,2,3]]
print(l2)
l3=[12,3,4]
l2.extend(l3)
print(l2)
#comprehensions
matrix=[]
for x in range(4):
    matrix.append([])
    for y in range(4):
        matrix[x].append(y)
print(matrix)
matrix=[[y for y in range(4)] for x in range(4)]
print(matrix)
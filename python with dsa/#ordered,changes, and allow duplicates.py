#ordered,changes, and allow duplicates
l1=[10,20,30,40,50]
print(l1)
l1[2]='apple'
print(l1)
l1[1:4]=['a','b','c','d','e']
print(l1)
#//////////////////////////////////
# create ,remove, items in a list:
#print(dir(l1))
l1.append('lakshmi')
print(l1)#insert(index,items)
l1.insert(2,'Mango')
print(l1)
#extend(collection)
l2=['A','B','C']
l1.extend(l2)
print(l1)
l1=[1,2]
l2=[2,3]
for x in l2:
    l1.append(l2)
    print(l1)
l=[10,20,3,4,50,68,40]
print(l)
#remove
l.remove(68)
l.pop(2)
print(l)
l.pop()
print(l)
del l[2:6]
print(l)
l.clear()
print(l)


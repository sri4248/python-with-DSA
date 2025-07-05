#list remaining methods
l1=['Bananas','papayas','Cherries','Apples','cherries','Cherries']
print(l1)
print(l1.index('cherries'))
print(l1.count('cherries'))
print(l1[::-1])
l1.reverse()
print(l1)
#sort ,and copy
l1.sort()
print(l1)
#desending order
l1.sort(reverse=True)
print(l1)
#capital letter starting
print(ord('C'))
print(ord('a'))
#state what function do want
l1.sort(key=str.lower)
print(l1)
l2=l1.copy()
print(l1)
print(l2)
l1.append(10)
print(l1)
print(l2)
l2.clear()
print(l1)
print(l2)
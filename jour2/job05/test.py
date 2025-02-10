def modifier(liste):
    liste.append(99)

l = [1,2,3]
l2 = l
modifier(l2)
print(l2)
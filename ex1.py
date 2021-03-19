L = [17, 38, 10, 25, 72, 45, 14]
"""
print(L)
"""
# question1
"""
for i in L:
    L[i]=L[i]+1
"""
# question2
print(L)
L.extend([12, 13])
print(L)
"""
# question3

print("l'indice de 72 est", L.index(72))

# Question 4
paires = []
impaires = []
for i in range(len(L)):

    if L[i] % 2 == 0:
        paires.append(L[i])
    else:
        impaires.append(L[i])

print("le tableau des paires est\n", paires)
print("le tableau des impaires est\n", impaires)
"""

# Question 5
L.insert(4, 30)
print(L)
# Question 6
if 30 in L:
    L.remove(30)
print(L)
# Question 7
L.reverse()
print(L)
# Question 8

nbr = int(input("Donner un nombre au hasard:    "))
if nbr in L:
    print("ce nombre existe")
else:
    print("ce nombre nexiste pas")

# Question 9 et 10:
l1 = L[2:4]
print("du 2ème au 3ème élément", l1)
l2 = L[:3]
print("du début au 2ème", l2)
# Question 11:
print(L[-1])



# from collections import Counter
c = input("saisir votre chaine    ")
print("--------------------------")
# question 1-------------------------
# à chaque fois on teste sur un caractere different
if "z" in c:
    
    print("ce caractere existe!")
else:
    print("ce caractere n'exsite pas!")
print("--------------------------")
# question 2-------------------------------
print("le nbr de caractere desiré est", c.count('e'))
print("--------------------------")
# question 3----------------------------------
txt = c[::-1]
print(txt)
print("--------------------------")
# question 4---------------------------------
"""def ispalindrome(s):
    return s == s[::-1]

# skip
res = ispalindrome(c)"""
"""
# question 4 palindrome solution 2
if txt == c:
    print("chaine  palindrome")
else:
    print("chaine  non palindrome")
"""
print("--------------------------")
# question 5-------------------------------------------
def compteur_mots(s):
    return len(c.split())


print("le nbr de mots est", compteur_mots(c))
print("--------------------------")
# questions 6---------------------------------------------

"""
def nb_occurence(t):

    nbocc = Counter(c)
    
    
    return nbocc

print("Le nombre d'occurence de chaque caractere est :\n "
      + str(nb_occurence(c)))
"""
# q6-----------------------------
def nb_occurrences(t):
    dictionary = {}

    i = 0
    for i in range(len(t)):
        if t[i] not in dictionary:
            if t.count(t[i]) > 1:
                dictionary[t[i]] = t.count(t[i])
    return dictionary

print(nb_occurrences(c))
print("--------------------------")
# Q7-------------------------------------------------------
def nb_occurrences2(t):
    dictionary = {}
    i = 0
    for i in range(len(t)):
        if t[i] not in dictionary:
            listchar = []
            x = t[i]
            if t.count(t[i]) > 1:
                for i in range(len(t)):
                    if t[i] == x:
                        listchar.append(i)
                dictionary[x] = listchar
    return dictionary

print(nb_occurrences2(c))
print("--------------------------")
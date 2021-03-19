from collections import Counter

c = input("saisir votre chaine    ")
print("la chaine de crt est", c)
# question 1
# à chaque fois on teste sur un caractere different
if "z" in c:
    print("ce caractere existe!")
else:
    print("ce caractere n'exsite pas!")
# question 2
print("le nbr de caractere est", c.count('e'))
# question 3
txt = c[::-1]
print(txt)

# question 4
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


# question 5
def compteur_mots(s):
    return len(c.split())


print("le nbr de mots est", compteur_mots(c))

# questions 6


def nb_occurence(t):
    nbocc = Counter(c)

    return nbocc


print("Le nombre d'occurence de chaque caractere est :\n "
      + str(nb_occurence(c)))

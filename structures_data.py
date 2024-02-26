# Listes
liste_1 = [1, 4, 2, 9]
villes = ["Paris", "Québec", "Cotonou", "Bruxelles", "Londres"]
others = [liste_1, villes]

# Indexing
# Premier élément
print(liste_1[0])
# Dernier élément
print(liste_1[-1])
# Avant dernier élément du tableau de liste
print(liste_1[-2])

print(villes)
print(others)

# Tuplej
tuple_1 = (1, 5, 8, 9, 7)
print(tuple_1)

# String
prenom = 'Nicolas'
print(prenom)

# Slicing
print(villes[0:1])
# ou
print(villes[:1])
print(villes[:3])
print(villes[2:])
print(villes[::2])
print(villes[::-1])

# append
villes.append("Dublin")
print(villes)

# insert
villes.insert(1, 'Madrid')
print(villes)

# extend
villes_2 = ["Amsterdam", "Rome"]
villes.extend(villes_2)
print(villes)

# len
print(len(villes))

# sort
villes.sort()
print(villes)
villes.sort(reverse=True)
print(villes)

# count
print(villes.count("Paris"))

# x = 1
# print(x)
# print(False & True)
# print(False | True)
# print(False ^ True)

f = lambda x: x**2
z = lambda x, y: x**2 + y

print(f(3))
print(z(3, 1))


def e_potentielle(masse, hauteur, g=9.81):
    E = masse * hauteur * g
    return E

print(e_potentielle(masse=80, hauteur=5))


def e_potentielle_one(masse, hauteur, e_limite, g=9.81):
    E = masse * hauteur * g
    if E > e_limite :
        return "L'énergie potentielle calculée est supérieure à l'énergie limite !"
    else :
        return "L'énergie potentielle calculée est inférieure à l'énergie limite !"

print(e_potentielle_one(masse=80, hauteur=5, e_limite=5000))
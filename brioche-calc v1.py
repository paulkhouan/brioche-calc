print'Bienvenue dans le calculateur de brioche. ')
qt_farine = float(input('Veuillez entrer la quantite de farine en grammes: '))

# calcule des pourcentages des autres ingredient selon la recette suivante:
# farine = 100, lait = 40, sucre = 16, sel = 2, oeuf = 0.4 (2 oeufs pour 500g de farine)

print('La quantite de lait necessaire est: ' + str(qt_farine * 40 / 100))
print('La quantite de sucre necessaire est: ' + str(qt_farine * 16 / 100))
print('La quantite de sel necessaire est: ' + str(qt_farine * 2 / 100))
print('La quantite en unite oeuf est: ' + str(qt_farine * 0.4 / 100))
print('La quantite de levure necessaire est: ' + str(qt_farine * 2 / 100))

# version V1 successful.
# prochaine etape, donner le choix de l'ingredient de base. Ex: si j'ai x quantite de lait...

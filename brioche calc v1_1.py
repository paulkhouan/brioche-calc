print('Bienvenue dans le calculateur de brioche v1.1 ')
ing_base = input('Quel ingredient de base?: (F)arine, (L)ait, (S)ucre, (O)euf ?: ')

if ing_base.upper() == "F":
   qt_farine = input("Veuillez entrer la quantite de farine en grammes: ")
   print('La quantite de lait necessaire est: ' + str(float(qt_farine) * 40 / 100))
   print('La quantite de sucre necessaire est: ' + str(float(qt_farine) * 16 / 100))
   print('La quantite de sel necessaire est: ' + str(float(qt_farine) * 2 / 100))
   print('La quantite en unite oeuf necessaire est: ' + str(float(qt_farine) * 0.4 / 100))
   print('La quantite de levure necessaire est: ' + str(float(qt_farine) * 2 / 100))
if ing_base.upper() == "L":
   qt_lait = input("Veuillez entrer la quantite de lait en grammes: ")
   qt_farine = float(qt_lait) * 100 / 40
# pour rendre facilite la tache, je fais le produit en croix du lait pour la farine,
# puis base tous les autres calculs sur la farine, ce qui mer permet de garder les memes formules tout du long.
   print('La quantite de farine necessaire est: ' + str(qt_farine))
   print('La quantite de sucre necessaire est: ' + str(float(qt_farine) * 16 / 100))
   print('La quantite de sel necessaire est: ' + str(float(qt_farine) * 2 / 100))
   print('La quantite en unite oeuf necessaire est: ' + str(float(qt_farine) * 0.4 / 100))
   print('La quantite de levure necessaire est: ' + str(float(qt_farine) * 2 / 100))
if ing_base.upper() == "S":
   qt_sucre = input("Veuillez entrer la quantite de sucre en grammes: ")
   qt_farine = float(qt_sucre) * 100 / 16
   print('La quantite de farine necessaire est: ' + str(qt_farine))
   print('La quantite de lait necessaire est: ' + str(float(qt_farine) * 40 / 100))
   print('La quantite de sel necessaire est: ' + str(float(qt_farine) * 2 / 100))
   print('La quantite en unite oeuf necessaire est: ' + str(float(qt_farine) * 0.4 / 100))
   print('La quantite de levure necessaire est: ' + str(float(qt_farine) * 2 / 100))
if ing_base.upper() == "O":
   qt_oeuf = input("Veuillez entrer la quantite d'oeufs en unite: ")
   qt_farine = float(qt_oeuf) * 100 / 0.4
   print('La quantite de farine necessaire est: ' + str(qt_farine))
   print('La quantite de lait necessaire est: ' + str(float(qt_farine) * 40 / 100))
   print('La quantite de sel necessaire est: ' + str(float(qt_farine) * 2 / 100))
   print('La quantite de sucre necessaire est: ' + str(float(qt_farine) * 16 / 100))
   print('La quantite de levure necessaire est: ' + str(float(qt_farine) * 2 / 100))
else:
   print("Veuillez recommencer avec F, L, S ou O. ")

# j'ai oublie le beurre !! la prochaine version 1.12 devra corriger le bug.

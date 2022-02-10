print('Bienvenue dans le calculateur de brioche v1.2 ')
ing_base = input('Quel ingredient de base?: (F)arine, (L)ait, (S)ucre, (O)euf (B)eurre?: ')
# farine = 58.14%, lait = 23.26%, sucre = 9,3%, beurre = 6.98%, sel = 1.16%, Levure = 1.16%, oeuf = 0.4/172
# poids total 172g pour 0.4 unite brioche
if ing_base.upper() == "F":
    qt_farine = input("Veuillez entrer la quantite de farine en grammes: ")
    qt_farine = float(qt_farine) * (58.14 / 100)
    qt_lait = float(qt_farine) * (23.26 / 100)
    qt_sucre = qt_farine * (9.3 / 100)
    qt_beurre = qt_farine * (6.98 / 100)
    qt_sel = qt_farine * (1.16 /100)
    qt_levure = qt_farine * (1.16 /100)

# changement de direction. Utiliser comme mesure de base la briche unitaire

    print(qt_lait)



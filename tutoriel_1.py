"""
-Récupérer ce que saisit l'utilisateur.
-Tester si c'est un nombre.
-si oui, continuer, afficher la table de multiplication, et demander à l'utilisateur
s'il souhaite quitter le programme ou non.
-Si non, arrêter la boucle et demander à l'utilisateur de saisir un nombre.
"""
continuer='o'
while continuer == 'o':
    user_typing= input("Entrez un nombre svp: ")
    test_typing= user_typing.isdigit()
    if test_typing:
        for i in range(11):
            print("{}*{}={}".format(int(user_typing), i, int(user_typing)*i))
        continuer= input("Voulez vous continuer? o/n ")
    else:
        print("Svp saisissez un autre nombre: ")

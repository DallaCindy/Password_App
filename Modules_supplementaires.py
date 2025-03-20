Choix_menu = [
       "A : Generer un nouveau mot d passe",
       "B : Voir un mot de passe specifique",
       "C : Voir tout les mots de passe enregistres"
    ]
liste=["A", "B", "C"]
def Choix_menu():
    for lettre in liste : 

def choix_caracteres(choix) :
    if choix.lower() != True and choix.lower() != False :
        print("Reponder par True ou False!!")
    else :
        print("Okay")
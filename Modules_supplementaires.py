Choix_menu = {
    "A" : "Generer un nouveau mot d passe",
    "B" : "Voir un mot de passe specifique",
    "C" : "Voir tout les mots de passe enregistres"
}

def choix_menu(choix):
    for lettre in Choix_menu : 
        if choix.upper() == lettre :
            return True
    return False




def choix_caracteres(choix) :
    if choix == "True" or choix == "False" :
        print("Okay")
    else :
        print("Reponder par True ou False!!")
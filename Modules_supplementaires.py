Choix_menu = {
       "A" : "Generer un nouveau mot d passe",
       "B" : "Voir un mot de passe specifique",
       "C" : "Voir tout les mots de passe enregistres"
}
liste=["A", "B", "C"]
def choix_menu(choix):
    for lettre in liste : 
         if choix.upper() == lettre :
            choix = Choix_menu[lettre]
            return choix
         else :
             return "entrer l'une des lettres suivantes pour effectuer une opration dans celles enumeres plus haut"
        
    
        

def choix_caracteres(choix) :
    if choix.lower() != True and choix.lower() != False :
        print("Reponder par True ou False!!")
    else :
        print("Okay")
from Modules_supplementaires import choix_menu,choix_caracteres
from Generateur_Password import generateur_password
print("bienvenue cher utlisateurs et merci de nous avoir choisi")
Choix_menu = [
       "A : Generer un nouveau mot d passe",
       "B : Voir un mot de passe specifique",
       "C : Voir tout les mots de passe enregistres"
    ]
choix = input(f":Quelles oprations parmi les suivantes souhaitez vous effectue : {Choix_menu}")
print("ecrivez uniquement la lettre de l'operation souhaitee")
result = choix_menu(choix)
print(result)

liste_Password ={
1 :"G4xLpM8d!",
2 :"P@ssw0rdK1ng",
3 :"L3ttr3sM4g1qu3s",
4 : "S3cur1tYp@ss",
5 : "M0nt4g3sP@ssw0rd",
6 : "F4nt4st1cP@ss",
7 : "R3v3l4t10nS3cr3t",
8 : "C0d3s3cur1tY",
9 : "P@ssw0rdM4g1c",
10 : "S3cur1t3P@ssw0rdL3v3l"}
if choix == Choix_menu[0] :
    longeur = int(input("Ecrivez la longueur du mot de passe que vous souhaitez (entre 8 et 32 caracteres) :  "))
    resultat = generateur_password(longueur=longeur)
    print(resultat) 

if choix == Choix_menu[1] :

    choix_miniscule = input( "\
      Souhaitez vous des lettres en miniscules dans votre mot de passe? \n\
      repondez par True ou par False\
    ")
    reponse1 = choix_caracteres(choix=choix_miniscule)
    print(reponse1)
    
    choix_majuscule = input( "\
      Souhaitez vous des lettres en majuscules dans votre mot de passe? \n\
      repondez egalement par True ou par False\
    ") 
    reponse2 = choix_caracteres(choix=choix_majuscule)
    print(reponse2)

    reponse1 = choix_caracteres(choix=choix_miniscule)
    print(reponse1)
    
    choix_chiffres = input( "\
      Souhaitez vous des chiffres dans votre mot de passe? \n\
      repondez encore par True ou par False\
    ") 
    reponse3 = choix_caracteres(choix=choix_chiffres)
    print(reponse3)

    liste_caracteres = [ "!@#$%^&*()_+-=[]{}|;:,.<>?"]
    choix_caractere = input( f"\
      Souhaitez vous des caracteres {liste_caracteres} dans votre mot de passe? \n\
      repondez encore par True ou par False\
    ") 
    reponse4 = choix_caracteres(choix=choix_caractere)
    print(reponse4)
    
    longeur = int(input("Ecrivez la longueur du mot de passe que vous souhaitez (entre 8 et 32 caracteres) :  "))
    resultat = generateur_password(longueur=longeur)
    print(resultat) 
    
    











import random
import string
import secrets
def generateur_password(longueur):
    if longueur < 8 or longueur > 32 :
        return "la longueur du mot de passe que vous souhaitez generer doit etre compris entre 8 et 32 caracteres!"
# Définir les ensembles de caractères
    miniscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    caracteres_speciaux = "!@#$%^&*()_+-=[]{}|;:,.<>?"
# S'assurer que le mot de passe contient au moins un caractère de chaque type
    mot_de_passe = [
        random.choices(miniscules),
        random.choices(majuscules),
        random.choices(chiffres),
        random.choices(caracteres_speciaux)
    ]
# Remplir le reste du mot de passe avec des caractères aléatoires
    tout_les_caracteres = miniscules + majuscules + chiffres + caracteres_speciaux
    mot_de_passe += random.choices(tout_les_caracteres, k=longueur - 4)
# Mélanger le mot de passe final pour plus de sécurité
    random.shuffle(mot_de_passe)
    mot_de_passe = str(mot_de_passe)
    return ''.join(mot_de_passe)


# longueur_du_mot_de_passe = 15  # Vous pouvez changer la longueur ici
# mot_de_passe_genere = generateur_password(longueur_du_mot_de_passe)
# print("Mot de passe généré :", mot_de_passe_genere)

def generateur_password_specifiques(longueur) : 
    if longueur < 8 or longueur > 32 :
        return "la longueur du mot de passe que vous souhaitez generer doit etre compris entre 8 et 32 caracteres!"
    
    if choix_miniscule == True :
      miniscules = string.ascii_lowercase
    if choix_majuscule == True :
      majuscules = string.ascii_uppercase
    if choix_chiffre == True :
      chiffres = string.digits
    if choix_caractere == True : 
      caracteres_speciaux = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    mot_de_passe = [
        random.choices(miniscules),
        random.choices(majuscules),
        random.choices(chiffres),
        random.choices(caracteres_speciaux)
    ]
# Remplir le reste du mot de passe avec des caractères aléatoires
    tout_les_caracteres = miniscules + majuscules + chiffres + caracteres_speciaux
    mot_de_passe += random.choices(tout_les_caracteres, k=longueur - 4)
# Mélanger le mot de passe final pour plus de sécurité
    random.shuffle(mot_de_passe)
    mot_de_passe = str(mot_de_passe)
    return ''.join(mot_de_passe)
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
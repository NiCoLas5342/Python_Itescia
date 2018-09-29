import math

def recup(a):
    """ récupère les deux derniers chiffres de l'année """
    a = a[2:4]
    return a

def div(a,b):
    """divise les deux derniers chiffres de l'année par 7 (retourne un nombre entier) et ajout du jour au compteur  """
    x = a//4
    x+=a+b
    return x



def Choix_Mois(Mois):
    """ retourne le nombre a ajouter en fonction du moi """
    if (Mois == "Janvier" or Mois == "Octobre"):
        return 0
    elif (Mois == "Mai" ):
        return 1
    elif (Mois == "Août"):
        return 2
    elif (Mois == "Février " or Mois == "Mars" or Mois == "Novembre"):
        return 3
    elif (Mois == "Juin"):
        return 4
    elif (Mois == "Septembre" or Mois == "Décembre"):
        return 5
    elif (Mois == "Juillet" or Mois == "Avril"):
        return 6
 


def bissextile(a,b):
    """ retourne le nombre a ajouter en fonction de l'année bissextile et le mois """
    if not(a%4==0):
        return 0
    elif not(a%100==0 )and(b == "Janvier" or b=="Février "):
        return 1
    elif not(a%400==0):
        return 0
    elif(b == "Janvier" or b=="Février ") :
        return 1
    
def Compte_annee(a):
    """ retourne le nombre a ajouter en fonction de l'année """
    res = a[0:2]
    if(res =='19'):
        return 0
    elif (res =='18'):
        return 2
    elif (res =='17' or res == '21'):
        return 4
    elif (res =='16' or res == '20'):
        return 6


def Trouver_Jour(a):
    """ récupère le reste et retourne la jour attendu"""
    x = a%7
    if (x==0):
        return "Dimanche"
    elif (x==1):
        return "Lundi"
    elif (x==2):
        return "Mardi"
    elif (x==3):
        return "Mercredi"
    elif (x==4):
        return "Jeudi"
    elif (x==5):
        return "Vendredi"
    elif (x==6):
        return "Samedi"

Jour = int(input("Veuillez selectionner le jour (ex : 12 ) : "))
Mois = input("Veuillez selectionner le moid (ex : Juillet ) : ")
Annee = input("Veuillez selectionner l'année (ex : 2012 ) : ")
""" éxecute les fonctions """
x = recup(Annee)
""" transforme un 'str' en 'int'pour faire les calculs ..."""
x = int(x)  
x = div(x,Jour)
x+= Choix_Mois(Mois)
Annee_int= int(Annee)
x-= bissextile(Annee_int,Mois)
x+= Compte_annee(Annee)
x = Trouver_Jour(x)
print("le",Jour,"/",Mois,"/",Annee,"correspond au jour de la semaine suivant: ",x)




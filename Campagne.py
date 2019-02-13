##############################
# Chanourdie Nicolas         #
# M2I L3 Cyber/Dev           #
# 13/02/19                   #
##############################

from tkinter import *
import os
import os.path
import re
import csv
import smtplib


# INTERFACES GRAPHIQUES #
#########################



# Interface pour ouvrir ou creer un nom de campagne
def CreationCampagne():
    fenetre = Tk()
    fenetre.title('CAMPAGNE')
    fenetre.geometry("400x300-10+100")
    champ_label = Label(fenetre, text="Nom de Campagne")
    champ_label.pack()
    var_texte = StringVar()
    ligne_texte = Entry(fenetre, textvariable=var_texte, width=20)
    ligne_texte.pack()
    bouton_ok = Button(fenetre, text="Crée la campagne", command=lambda:checkExistFile(var_texte.get(),fenetre))
    bouton_ok.pack(side="bottom")
    fenetre.mainloop()
 


    
# Interface pour gerer les adresses mails
def Accueil(fichier = ''):
    fenetre = Tk()
    fenetre.title('CAMPAGNE')
    fenetre.geometry("400x300-10+100")
    bouton_Ded = Button( text="Dedoubler", fg="green",command=lambda:Dedoubler(listbox))
    bouton_Ded.place(x=10, y=10, width=100, height=50)
    bouton_Val = Button( text="Valider", fg="green",command=lambda:Valider(listbox))
    bouton_Val.place(x=290, y=10, width=100, height=50)
    bouton_Csv = Button(text="Importer CSV", fg="red", command=lambda:VueCsv(listbox))
    bouton_Csv.place(x=10, y=80, width=100, height=50)
    bouton_Url = Button( text="Import URL", fg="red")
    bouton_Url.place(x=290, y=80, width=100, height=50 )#Fonctionne pas 
    bouton_Suite = Button( text="Suite", fg="red" , command=lambda:Suite(fenetre))
    bouton_Suite.place(x=320, y=260, width=50, height=30)
    listbox = Listbox(fenetre)
    listbox.pack()
    fenetre.mainloop()
    return fenetre 

#Interface pour gerer l'expediteur (En cours de programmation ...) 
def Expedition():
    fenetre = Tk()
    fenetre.title('CAMPAGNE')
    fenetre.geometry("400x300-10+100")
    var_texte = StringVar()
    champ_Exp = Label(fenetre, text="Expediteur : ")
    champ_Exp.place(x=-70, y=10, width=350, height=30)
    ligne_Exp = Entry(fenetre, textvariable=var_texte, width=20)
    ligne_Exp.place(x=170, y=10, width=150, height=30)
    champ_Obj = Label(fenetre, text="Objet : ")
    champ_Obj.place(x=-70, y=50, width=350, height=30)
    ligne_Obj = Entry(fenetre, textvariable=var_texte, width=20)
    ligne_Obj.place(x=170, y=50, width=150, height=30)
    champ_Message = Label(fenetre, text="Message")
    champ_Message.place(x=-70, y=100, width=350, height=30)
    ligne_Mess = Entry(fenetre, textvariable=var_texte, width=20)
    ligne_Mess.place(x=170, y=100, width=150, height=150)
    bouton_Suite = Button( text="Suite", fg="red")
    bouton_Suite.place(x=320, y=260, width=50, height=30)
    fenetre.mainloop()


#Interface pour gerer l'import de fichier.csv
#Le fichier doit etre dans le meme dossier que celui du projet 
def VueCsv(listbox):
    fenetre = Tk()
    fenetre.title('Importation CSV')
    File=Entry(fenetre,width=20)
    Import=Button(fenetre,text="Importer",command=lambda:importcsv(listbox,File.get(),fenetre))
    File.pack()
    Import.pack()   
    fenetre.mainloop()


    

# DEFINITION UTILISÉES POUR  LES INTERFACES #
#############################################

def checkExistFile(fileName, fenetre):

    my_file = "/Users/nicolas/Desktop/"+fileName
    if os.path.exists(my_file):
        fenetre.destroy()
        Accueil(fichier=my_file)
    else:
        fenetre.destroy()
        Ecrire(my_file, "")
        Accueil()
    return fenetre
        
def Ecrire(fichier,mail):
      with open(fichier, "a") as fichier:
          fichier.write(mail+'\n')
          
def Lire(fichier) :
       with open(fichier, 'r') as fichier :
           texte = print (fichier.read())
           print (texte)
           text = fichier.read()
       return text
    
def importcsv(listbox,file,fenetre4):
    if file.endswith(".csv")==False:
        file=file+".csv"
    with open(file, 'r', encoding="utf-8") as file:
        spamreader = csv.reader(file)
        column=[]
        for row in spamreader:
            column+=row[0].split("\t")
        for i in range(len(column)):
            listbox.insert(END,column[i])
    fenetre4.destroy()


def Dedoubler(listbox):
    Mails=listbox.get(0,listbox.size()-1)
    listbox.delete(0,listbox.size()-1)
    element=list(set(Mails))
    for i in range (len(element)):
        listbox.insert(END,element[i])

def Valider(listbox):
    maxrange=listbox.size()
    for i in range (maxrange):
        if mailsValide(listbox.get(i))==False:
            listbox.delete(i)
            
       
        
def mailsValide(email):
    return email.find("@")>0 and email.find(".fr")>0 or email.find(".com")>0    


def Suite(fenetre):
    fenetre.destroy()    
    Expedition()
    
fenetre=CreationCampagne()
fenetre2=Accueil()
fenetre3=Expedition()
fenetre4=VueCsv()
fenetre5=VueUrl()

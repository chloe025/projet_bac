from tkinter import *
from tkinter import font  # tkinter n'importe pas font automatiquement
from tkinter.messagebox import askyesno  # importe fenetre yes/no
from random import randrange
import pygame
from math import sqrt
import tkinter as tk

pygame.init()

##################################
# création des variables de base #
##################################
quitte = True
compteur = 50
nombre, points, erreur, score, b, vieuxscore = 0, 0, 0, 0, 0, 0
a = randrange(2, 200)


##########################
# Création des fonctions #
##########################
# Fonctions Principales du Programme :
# création d'un nouveau nombre à de nouvelles coordonées
def nvNB():
    global a, coordX, coordY, nombre
    a = randrange(2, 2000)
    nbalea.config(text=str(a), bg='#82FA58')
    coordX, coordY = randrange(5, 1220), randrange(5, 570)
    testnbpre()  # effectue le test du nombre premier sur "a"


# test du nombre premier "a"
def testnbpre():
    global nombre
    b = 0
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            b = 1
    if b == 0:
        nombre = 3  # le nombre "a" est premier
    else:
        nombre = 2  # le nombre "a" n'est pas premier


# Fonctions des zones de clic Gauche et Droit :
def GereClickG(event):
    global points, erreur

    if nombre == 3:
        points = points + 1
        affichescoreP.config(
            text="Bonne Réponses : " + str(points))
        print('nombre premier touché')
        sonrep = pygame.mixer.Sound("images/Win.wav")
        sonrep.play()
    else:
        erreur = erreur + 1
        affichescoreE.config(text='Erreurs : ' + str(erreur))
        print('c\'était pas un nombre premier')
        sonerreur = pygame.mixer.Sound("images/erreur.wav")
        sonerreur.play()
    nvNB()
    nbalea.place(x=coordX, y=coordY, width=80, height=50)


def GereClickD(event):  # le clic droit = PAS DE NOMBRE PREMIER
    global points, erreur

    if nombre == 2:
        points = points + 1
        affichescoreP.config(text="Bonne Réponses : " + str(points))
        sonrep = pygame.mixer.Sound("images/Win.wav")
        sonrep.play()
        print("cest bien un autre nombre")
    else:
        erreur = erreur + 1
        affichescoreE.config(text='Erreurs : ' + str(erreur))
        sonerreur = pygame.mixer.Sound("images/erreur.wav")
        sonerreur.play()
        print("c'etait un nombre premier")
    nvNB()
    nbalea.place(x=coordX, y=coordY)


#####################
# AUTTRES FONCTIONS #
#####################
# le chronomètre
def count():
    global compteur, quitte
    while compteur > 0:
        compteur = compteur - 1
        affichetemps.config(text="temps restant : " + str(compteur) + " s")
        affichetemps.after(1000, count)  # 1000ms = 1 sec. After permet de rappeler la fonction count
        break
    else:
        quitte = True
        terminer()
        nvNB()
        nbalea.destroy()

# fonctions pour les boutons
def retour():
    fenjeu.destroy()
    import menu


def quitter():  # ouvre une fenêtre de confirmation de fin de prog
    reponse = askyesno('Quitter le programme ?', 'Voulez-vous quitter le jeu ? \n Cliquez sur OUI pour quitter')
    if reponse == True:
        fenjeu.destroy()
    else:
        terminer()


def start():
    global quitte
    boutonstart.config(text="TERMINER", command=terminer)
    if quitte == True:
        quitte = False
        count()
        nvNB()
        nbalea.bind("<Button-1>", GereClickG)
        nbalea.bind("<Button-3>", GereClickD)
        zoneConsigne.destroy()
        nbalea.place(x=coordX, y=coordY, width=80, height=50)


def recommancer():
    # erreur bad window path name -> due a la destruction du nbalea. et invalid command name ".!label2"
    global score, points, erreur, compteur, quitte
    score, points, erreur, compteur = 0, 0, 0, 50
    nbalea = Label(fenjeu, text=str(a), font=fontjeu, bg='#82FA58')
    nvNB()
    nbalea.place(x=coordX, y=coordY, width=80, height=50)
    start()

def terminer():
    global compteur, score, quitte
    fontscore = font.Font(size=16, family='Comic Sans MS')
    compteur = 0
    if quitte == True:
        fenfin = Toplevel()
        fenfin.title('SCORE')
        fenfin.geometry('400x400')
        score = points - erreur * 2
        Label(fenfin, text='Partie Terminée : \n Bonnes Réponses : ' + str(points) + "\n Erreurs faites : "
                           + str(erreur) + " \n Score Total =" + str(score), font=fontscore).pack()
        boutonQuit = Button(fenfin, text='Quitter', command=quitter, font=mafont2, width=20).place(x=90, y=240)
        boutonstart.config(text="Recommencer !", command=recommancer)
        boutonaccueil = Button(fenfin, text="Accueil", command=retour, font=mafont2, width=20).place(x=90, y=300)
        son.stop()
        SaveScore()


def modif():
    fenjeu.destroy()
    import Doctor


def SaveScore():
    global vieuxscore
    if vieuxscore < score:
        fichierScore = open("fichierScore.txt", "w+")
        fichierScore.write(str(score))
        vieuxscore = score
        fichierScore.close()


#####################################
# création de la fenêtre principale #
#####################################
fenjeu = tk.Tk()
fenjeu.geometry('1300x700')
fenjeu.title('Etre ou ne pas etre ? Un nombre premier')
photo = PhotoImage(file="images/maths.png")
zone_dessin = tk.Canvas(fenjeu, width=1299, height=620, bg='yellow', )
zone_dessin.create_image(650, 300, image=photo)
zone_dessin.pack()
son = pygame.mixer.Sound("images/Mozart.wav")
son.play()

# création de la sous-fenêtre #
frameBas = Frame(fenjeu, borderwidth=4, relief=GROOVE, bg="#BDBDBD", width=1299, height=80)
frameBas.pack(side=BOTTOM)

# des fonts pour le jeu
mafont2 = font.Font(family='Arial', size=12, weight='bold')
fontjeu = font.Font(size=26, weight='bold')

# mise en place des widgets dans la Frame #
boutonfond = Button(frameBas, command=modif, justify='center', text='Quiz Doctor Who !', font=mafont2)
boutonfond.place(x=300, y=20, width=150, height=30)
boutonstart = Button(frameBas, command=start, justify='center', text='Commencer !', font=mafont2)
boutonstart.place(x=555, y=20, width=140, height=30)
affichetemps = Label(frameBas, text="temps restant : " + str(compteur) + " s", font=mafont2, fg='red')
affichetemps.place(x=10, y=10, height=45)
affichescoreP = Label(frameBas, text="Bonne Réponses : " + str(points))
affichescoreP.place(x=1100, y=5, height=25)
affichescoreE = Label(frameBas, text='Erreurs : ' + str(erreur))
affichescoreE.place(x=1100, y=40, height=25)

# affichage de la zone de consigne
zoneConsigne = Label(fenjeu, text='Touchez les nombres premiers \n avec clic GAUCHE, \n sinon clic DROIT ! \n '
                                  'Attention, -2 points pour \n chaque erreur \n Cliquez sur le bouton "commencer"',
                     font=fontjeu, fg='red', bg='#E2A9F3',
                     takefocus=True, state="normal", activebackground="#808080", activeforeground="#2EFE2E")
zoneConsigne.place(x=300, y=110, width=750, height=300)
zoneConsigne.bind("<Enter>", lambda x=None:
zoneConsigne.config(state="active"))
zoneConsigne.bind("<Leave>", lambda x=None:
zoneConsigne.config(state="normal"))

# création zone de texte pour le nombre "a"
nbalea = Label(fenjeu, text=str(a), font=fontjeu, bg='#82FA58')

fenjeu.mainloop()

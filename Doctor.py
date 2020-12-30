from tkinter import *
from tkinter import font
import copy
import pygame
pygame.init()

son = pygame.mixer.Sound("images/ThemeDW.wav")
son.play()

n = 0
score = 0
bonnerep = False

listeQuestion = ["De quelle planète vient-il ?", "Quelle est son arme préférée ?",
                 "Lequel est son vaisseau ?",
                 "Que signie l'acronyme TARDIS ?", "Quel est la phrase préférée du 10e Docteur ?",
                 "Qui est l'ennemi juré du docteur ? \n(plusieurs réponses possibles)"
    , "Où le docteur est-il censé mourir ?", "Qui n'a jamais été compagnon du Docteur ?",
                 "Comment Amy appelle-t-elle \nl'homme étrange de son enfance ?",
                 "Pourquoi le TARDIS fait-il son bruit caractéristique ?",
                 "Qui est Face de Bo ?", "Que trouve-t-on dans \nle Tardis du 13e Docteur ?",
                 "En quelle année a été diffusée pour la première \nfois Doctor Who à la télévision britannique ?"
    , "Que ne faut-il pas faire en présence d'Anges Pleureurs ?",
                 "Quel accessoire vestimentaire le \ndocteur Matt Smith adore-t-il porter ?",
                 "Qui est le plus 'jeune' docteur ?", "Qui a composé la musique du thème de la série ?",
                 "Comment le Docteur obtient-il son TARDIS ?",
                 "Que dit River pour rappeler au Docteur \n de ne pas lui poser de questions ?",
                 "Combien faut-il de personnes pour piloter\n"
                 "le TARDIS de façon "
                 "optimale ?",
                 "A quelle race appartient le Docteur ?",
                 "Quelle est la particularité du Tardis ? \n(plusieurs réponses possibles)",
                 "Quelle forme prend le camouflage du TARDIS ?"]
R1 = ["un seul, il est unique mais il s'est régénéré 13 fois", "7", "13 bien entendu", "12, il ne peut se régénérer que 12 fois"]
R2 = ["Tatooine", "Gallifrey", "Terre", "Proxima du Centaure"]
R3 = ["il ne possède pas d'arme", "un colt Woodsman", "un tournevis sonique", "une scie sauteuse ionisante"]
R4 = ["le Nexus VI", "le Prometheus", "le Nostromo", "le Tardis"]
R5 = ["Temps A Relativé Dimensionnelle Inter-Spatiale", "Toujours Aussi Riche Drole Intelligent et Séduisant",
             "Transporteur Alien Réservé aux Dimensions Inter-Spatiales",
             "Truc Absurde Reservé au Docteur Imaginaire Sénile"]
R6 = ["Géronimo !", "Hasta la vista baby !", "Allons-y !", "Ne cligne pas des yeux"]
R7 = ["les Daleks", "le Maître", "les Klingons", "le Silence"]
R8 = ["dans son Tardis", "sur Terre", "sur Gallifrey", "sur Trenzalore"]
R9 = ["Rose Tyler", "Amy Pond et Rory Williams", "Yasmine Khan, Ryan Sinclair, Graham O'Brien",
             "Clara Morgane", ]
R10 = ["L'homme clown", "Le Docteur débraillé", "L'homme nu", "Le Docteur de l'espace"]
R11 = ["c'est juste un bruit", "c'est le bruit du moteur", "le frein à main est serré", "un pièce moteur rare est abîmée"]
R12 = ["son ennemi juré", "un Seigneur du Temps", "Brian Williams", "Jack Harkness"]
R13 = ["un distributeur de biscuits", "une niche de chien", "un placard à balais", "un tableau noir"]
R14 = ["1965", "1983", "1985", "1963"]
R15 = ["faire du bruit", "leur parler", "cligner des yeux", "respirer"]
R16 = ["une veste en cuir", "des lunettes de soleil", "une canne", "un noeud-papillon", ]
R17 = ["Matt Smith", "David Tennant", "Peter Capaldi", "Jodie Whittaker"]
R18 = ["John Barry", "John Williams", "Ron Grainer", "Fletcher McCormick"]
R19 = ["il l'obtient à sa majorité","il l'a gagné après une partie de carte","il l'obtient en récompense après avoir gagné la Guerre du Temps","il le vole"]
R20 = [" \"Non, non, non\" ", " \"Je n'ai pas les réponses\" ", " \"Demandez-moi plus tard\" ",
              " \"C'est pas l'heure\" "]
R21 = ["4", "6", "1", "7"]
R22 = ["humaine", "Atraxis", "Seigneurs du Temps", "Guerriers des Glaces"]
R23 = ["il a fait le raid de Kessel en 12 parsec", "il est plus grand à l'intérieur",
              "il peut se déplacer n'importe où n'importe quand sans consommer d'énergie",
              "il permet de comprendre n'importe quelle langue"]
R24 = ["une cabine de police bleue", "un cylindre gris", "une cabine téléphonique rouge","un bateau corsaire spatial"]
listerep1,listerep2 = [1, 0, 0, 0],[0, 1, 0, 0]
listerep3, listerep4 = [1, 0, 0, 0], [0, 0, 0, 1]
listerep5,listerep6 = [1, 0, 0, 0],[0, 0, 1, 0]
listerep7, listerep8, listerep9 = [1, 1, 0, 1], [0, 0, 0, 1],[0, 0, 0, 1]
listerep10, listerep11, listerep12 = [0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]
listerep13, listerep14, listerep15 = [1, 0, 0, 0],[0, 0, 0, 1],[0, 0, 1, 0]
listerep16, listerep17, listerep18 = [0, 0, 0, 1],[1, 0, 0, 0],[0, 0, 1, 0]
listerep19, listerep20,listerep21 =  [0, 0, 0, 1],[0, 0, 0, 1],[0, 1, 0, 0]
listerep22, listerep23,listerep24 = [0, 0, 1, 0],[0, 1, 0, 1],[1, 0, 0, 0]
listerep = [listerep1, listerep2, listerep3, listerep4, listerep5, listerep6, listerep7, listerep8, listerep9, listerep10, listerep11, listerep12, listerep13
            , listerep14, listerep15, listerep16,listerep17, listerep18, listerep19, listerep20, listerep21, listerep22, listerep23, listerep24]
listeR = [ R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24]
listeRep1=["un seul, il est unique mais il s'est régénéré 13 fois", "7", "13 bien entendu", "12, il ne peut se régénérer que 12 fois"]



def validation():
    global n, score, listerep1, listeRep1
    actualise()
    Question.config(text=listeQuestion[n])
    Quest.config(text="Question : " + str(n))
    listeRep1.clear()
    print(listerep1)
    print("question",n)
    for i in range (n,22):
        listeRep1 = copy.copy(listeR[n])
        listerep1 = copy.copy(listerep[n])
    Reponse0.config(text=listeRep1[0])
    Reponse0.deselect()
    Reponse1.config(text=listeRep1[1])
    Reponse1.deselect()
    Reponse2.config(text=listeRep1[2])
    Reponse2.deselect()
    Reponse3.config(text=listeRep1[3])
    Reponse3.deselect()
    if bonnerep == False:
        score = score - 1
    else:
        score = score + 1
    n = n + 1


def actualise():
    global bonnerep, listerep1
    print(Reponse0)
    if listerep1[0] == 1 and listerep1[0] == v.get():
        print("premiere case cochée")
        bonnerep = True
    elif listerep1[1] == 1 and listerep1[1] == v1.get():
        print("2e case cochée")
        bonnerep = True
    elif listerep1[2] == 1 and listerep1[2] == v2.get():
        print("3e case cochée")
        bonnerep = True
    elif listerep1[3] == 1 and listerep1[3] == v3.get():
        print("4e case cochée")
        bonnerep = True
    elif listerep1[0] == 0 and listerep1[0] != v.get():
        bonnerep = False
        print("1er case cochée  : fausse")
    elif listerep1[1] == 0 and listerep1[1] != v1.get():
        bonnerep = False
        print("2e case cochée : fausse")
    elif listerep1[2] == 0 and listerep1[2] != v2.get():
        bonnerep = False
        print("3e case cochée  : fausse")
    elif listerep1[3] == 0 and listerep1[3] != v3.get():
        bonnerep = False
        print("4e case cochée  : fausse")


def termine():
    Question.destroy()
    Quest.destroy()
    Reponse0.destroy()
    Reponse1.destroy()
    Reponse2.destroy()
    Reponse3.destroy()
    Score = Label(fenjeu, text="Le score est de " + str(score) + " points sur 24", font=mafont).place(x=550, y=400)

def accueil ():
    fenjeu.destroy()
    son.stop()
    import menu

fenjeu = Tk()
fenjeu.geometry("1300x700")
fenjeu.title("Quizz")
fond = Canvas(fenjeu, width=1300, height=800)
photo = PhotoImage(file="images/dw1.png")
fond.create_image(650, 300, image=photo)
fond.pack()

mafont = font.Font(family='Arial', size=26, weight='bold')
fontrep = font.Font(family="Helvetica", size=16)
Quest = Label(fenjeu, text="Question : " + str(n), fg='red', font=mafont)
Quest.place(x=400, y=100)
Question = Label(fenjeu, text="Combien y a t-il de Docteurs ?", fg='blue', font=mafont)
Question.place(x=300, y=200)
valid = Button(fenjeu, text="Valider", command=validation).place(x=650, y=600)
quitter = Button (fenjeu, text="Quitter",command=fenjeu.destroy).place(x=20,y=20, width=50)
acc = Button(fenjeu, text="Accueil", command=accueil).place(x=20, y = 50, width=50)

v, v1, v2, v3 = IntVar(), IntVar(), IntVar(), IntVar()

Reponse0 = Checkbutton(fenjeu, text=listeRep1[0], variable=v, font=fontrep, command=actualise)
Reponse0.place(x=450, y=350)

Reponse1 = Checkbutton(fenjeu, text=listeRep1[1], variable=v1, font=fontrep, command=actualise)
Reponse1.place(x=450, y=400)

Reponse2 = Checkbutton(fenjeu, text=listeRep1[2], variable=v2, font=fontrep, command=actualise)
Reponse2.place(x=450, y=450)

Reponse3 = Checkbutton(fenjeu, text=listeRep1[3], variable=v3, font=fontrep, command=actualise)
Reponse3.place(x=450, y=500)

fenjeu.mainloop()

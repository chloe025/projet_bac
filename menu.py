from tkinter import *
from tkinter import font  # tkinter n'importe pas font automatiquement
import tkinter as tk

###############
# MENU DU JEU #
###############

# création du menu
fenprinci = tk.Tk()
fenprinci.geometry('1300x700')
fenprinci.title('CHICKEN RUN')
# Une font pour le titre
mafont = font.Font(family='Papyrus', size=32, weight='bold', )

canvas = tk.Canvas(fenprinci, width=1300, height=700)
canvas.pack()

# les frames qui vont acceuillir les boutons
frame = tk.Frame(canvas, width=50, height=5)
frame1 = tk.Frame(canvas, width=50, height=5)
frame2 = tk.Frame(canvas, width=50, height=5)
frame3 = tk.Frame(canvas, width=50, height=5)

photo = PhotoImage(file='images/fond1800x1400.png')
canvas.create_image(650, 350, image=photo)

# création de canvas sur le cansvas pour le titre et boutons
canvas.create_text((650, 100), text='le Meilleur Projet Bac !', font=mafont, fill='red', width=250)
canvas.create_window((650, 300), window=frame, anchor='center')
canvas.create_window((650, 400), window=frame1, anchor='center')
canvas.create_window((650, 500), window=frame2, anchor='center')


# création des fonctions pour ouvrir les différents boutons
def createjeu():
    fenprinci.destroy()
    import mode1


def createjeu2():
    fenprinci.destroy()
    import Doctor


# Création des Boutons
# button = tk.Button(frame, text='Hello World').pack()
boutonHistoire = tk.Button(frame, text='Pour les vrais Matheux', command=createjeu, width=40, height=2).pack()
boutonModeDW = Button(frame1, text='Pour les vrais Whoviens', command=createjeu2, width=40, height=2).pack()
boutonquitte = Button(frame2, text='Quitter', command=fenprinci.destroy, width=40, height=2).pack()

fenprinci.mainloop()

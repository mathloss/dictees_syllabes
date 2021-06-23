from tkinter import *
from random import choice
from random import shuffle 
import pyttsx3

root = Tk()
root.title("Dictée de syllabes")
root.configure(background='black')
root.geometry("400x600")
root.iconbitmap("C:/Users/eriol/Desktop/programmation/syllabes/alphabet.ico")

# --------------------------------LES FONCTIONS---------------------------------------------------
def nouveau_son():
    reponse_entry.delete(0,"end")
    liste_son = ["ba", "ca", "da" , "fa", "ga", "bi", "bo" ,"bu"]
    son1 =  choice(liste_son)
    son2 = choice(liste_son)
    global mot_a_trouver
    mot_a_trouver = son1 + son2
    print(mot_a_trouver)
    engine = pyttsx3.init()
    engine.setProperty('rate',100)
    engine.say(mot_a_trouver)
    engine.runAndWait()


def repeter_son():
    engine = pyttsx3.init()
    engine.setProperty('rate',100)
    engine.say(mot_a_trouver)
    engine.runAndWait()

def verifier():
    if reponse_entry.get() == mot_a_trouver:
        resultat_label.config(text="Gagné!!")
        resultat_label2.config(text=mot_a_trouver + " est juste !")
    else:
        resultat_label.config(text="Perdu...")
        resultat_label2.config(text="la solution : " + mot_a_trouver)



def syllabe_2():
    hide_menu_frame()
    root.geometry("400x600")
    syllabe_2_frame.pack(fill="both", expand=1)

    ecoute_frame = Frame(syllabe_2_frame, width=400, height=200, bg="black")
    ecoute_frame.pack(pady=5)

    label_1 = Label(ecoute_frame,text="Ecoute attentivement", font=("Arial",20), bg="black", fg="white")
    label_1.grid(row=0, column=0) 

    bouton_ecoute = Button(ecoute_frame, text="Son",font=("Arial",20), bg="black", fg="white",command=nouveau_son)
    bouton_ecoute.grid(row=0, column=1, padx=15)

    bouton_repeter = Button(syllabe_2_frame, text="Encore",font=("Arial",20), bg="black", fg="white",command=repeter_son)
    bouton_repeter.pack(pady=10)

    label_2 = Label(syllabe_2_frame, text="Ta réponse : ", font=("Arial",20), bg="black", fg="white")
    label_2.pack(pady=10)

    reponse_frame = Frame(syllabe_2_frame,width=400, height=200, bg="black")
    reponse_frame.pack(pady=10)

    global reponse_entry
    reponse_entry = Entry(reponse_frame, width=10,font=("Arial",32),justify="center", bg="black", fg="white")
    reponse_entry.grid(row=0, column=0)

    verifier_button= Button(reponse_frame, text="Vérifies",font=("Arial",20),justify="center", bg="black", fg="white",command=verifier)
    verifier_button.grid(row=0, column=1, padx=10)

    global resultat_label
    resultat_label = Label(syllabe_2_frame, text="Nul",font=("Arial",20), bg="black", fg="white") 
    resultat_label.pack(pady=10)

    global resultat_label2
    resultat_label2 = Label(syllabe_2_frame, text="TRES NUL",font=("Arial",20), bg="black", fg="white") 
    resultat_label2.pack(pady=10)
   
def syllabe_3():
    hide_menu_frame()
    root.geometry("400x600")
    syllabe_3_frame.pack(fill="both", expand=1)

def syllabe_4():
    hide_menu_frame()
    root.geometry("400x600")
    syllabe_4_frame.pack(fill="both", expand=1)
    

# fonction effacer frame
def hide_menu_frame():
    syllabe_2_frame.pack_forget()
    syllabe_3_frame.pack_forget()
    syllabe_4_frame.pack_forget()
    choix_frame.pack_forget()




# on crée le menu principal
mon_menu = Menu(root)
root.config(menu=mon_menu)

def choix():
    hide_menu_frame()
    choix_frame.pack(fill="both", expand=1)
    choix_label = Label(choix_frame, text=" Bienvenu(e) dans le jeu", font=("Arial",20), bg="black",fg="white")    
    choix_label.pack(pady=20)
    choix_label2 = Label(choix_frame, text=" de dictée de syllabes", font=("Arial",20), bg="black",fg="white")    
    choix_label2.pack(pady=20)
    s2_button = Button(choix_frame, text="2 syllabes", font=("Arial",20), bg="black",fg="white", command=syllabe_2) 
    s2_button.pack(pady=5)
    s3_button = Button(choix_frame, text="3 syllabes", font=("Arial",20), bg="black",fg="white", command=syllabe_3) 
    s3_button.pack(pady=5)
    s4_button = Button(choix_frame, text="4 syllabes", font=("Arial",20), bg="black",fg="white", command=syllabe_4) 
    s4_button.pack(pady=5)
   



# les items du menu
syllabe_menu = Menu(mon_menu)
mon_menu.add_cascade(label="Syllabes", menu=syllabe_menu)
syllabe_menu.add_command(label="2 syllabes", command=syllabe_2)
syllabe_menu.add_command(label="3 syllabes", command=syllabe_3)
syllabe_menu.add_command(label="4 syllabes", command=syllabe_4)
syllabe_menu.add_separator()
syllabe_menu.add_command(label="Quitter", command=root.quit)

# on crée les frames
syllabe_2_frame = Frame(root, width=400, height=600, bg="black")
syllabe_3_frame = Frame(root, width=400, height=600, bg="black")
syllabe_4_frame = Frame(root, width=400, height=600, bg="black")
choix_frame = Frame(root, width=400, height=600, bg="black")

choix()

root.mainloop()
    
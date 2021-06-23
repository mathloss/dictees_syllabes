from tkinter import *

root = Tk()
root.title("Dictée de syllabes")
root.iconbitmap("C:/Users/eriol/Desktop/syllabes/alphabet.ico")
root.geometry("400x400")
root.configure(background='black')


def syllabe_2():
    pass
def syllabe_3():
    pass
def syllabe_4():
    pass

# on crée le menu principal
mon_menu = Menu(root)
root.config(menu=mon_menu)

def choix():
    hide_menu_frame()
    choix_frame.pack(fill="both", expand=1)
    choix_label = Label(choix_frame, text=" Bienvenu(e) dans le jeu", font=("Arial",20), bg="black",fg="white")    
    choix_label.pack(pady=20)
    choix_label2 = Label(choix_frame, text=" dictée de syllabes", font=("Arial",20), bg="black",fg="white")    
    choix_label2.pack(pady=20)
    syllabe_2_button = Button(choix_frame, text="2 syllabes", font=("Arial",20), bg="black",fg="white", command=syllabe_2) 
    syllabe_2_button.pack(pady=5)
    syllabe_3_button = Button(choix_frame, text="3 syllabes", font=("Arial",20), bg="black",fg="white", command=syllabe_3) 
    syllabe_3_button.pack(pady=5)
    syllabe_4_button = Button(choix_frame, text="4 syllabes", font=("Arial",20), bg="black",fg="white", command=syllabe_4) 
    syllabe_4_button.pack(pady=5)
  
    l6_button.pack(pady=5)


# fonction effacer frame
def hide_menu_frame():
    syllabe_2_frame.pack_forget()
    syllabe_3_frame.pack_forget()
    syllabe_4_frame.pack_forget()
    choix_frame.pack_forget()


# les items du menu
syllabe_menu = Menu(mon_menu)
mon_menu.add_cascade(label="Dictée de syllabes", menu=mon_menu)
syllabe_menu.add_command(label="2 syllabes", command=syllabe_2)
syllabe_menu.add_command(label="3 syllabes", command=syllabe_3)
syllabe_menu.add_command(label="4 syllabes", command=syllabe_4)
syllabe_menu.add_separator()
syllabe_menu.add_command(label="Quitter", command=root.quit)

# on crée les frames
syllabe_2_frame = Frame(root, width=400, height=400, bg="black")
syllabe_3_frame = Frame(root, width=400, height=400, bg="black")
syllabe_4_frame = Frame(root, width=400, height=400, bg="black")
choix_frame = Frame(root, width=400, height=400, bg="black")

choix()


root.mainloop()
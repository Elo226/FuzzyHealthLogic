import tkinter as tk
from tkinter import ttk
from devoir import *

# Classe PageAccueil
class PageAccueil(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Page d'accueil")
        self.geometry("1000x666")
        
        # Charger l'image de fond
        self.background_image = tk.PhotoImage(file="img.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        s = ttk.Style()
        s.configure('My.TFrame', background='#f0f0f0', font=("Helvetica", 14))
        s.configure('My.TLabel', background='#f0f0f0', font=("Helvetica", 14), foreground='black')
        
        self.accueil_frame = ttk.Frame(self, padding=50, relief='solid', borderwidth=1, style='My.TFrame')
        self.accueil_frame.pack(pady=15, expand=True)

        self.button_quitter = tk.Button(self, background="red", font=("Helvetica", 18, "bold"), text="Quitter", command=self.close_Accueil)
        self.button_quitter.pack(pady=10, expand=True)
        
        self.create_widgets()

    def create_widgets(self):
        self.msg_bienvenu = tk.Label(self.accueil_frame, text="BIENVENU SUR SANTE PLUS +", font=("Helvetica", 25, "bold", "italic"), foreground="blue", background="#C2F100")
        self.msg_bienvenu.grid(row=0, column=2, pady=10, sticky='nsew')
        
        # Pour centrer les boutons, nous utilisons 'center' comme valeur pour sticky
        self.button_pression = tk.Button(self.accueil_frame, text="Pression Artérielle", command=self.open_PressionFrame, font=("Helvetica", 18, "bold"), background="#00CBE9")
        self.button_pression.grid(row=1, column=2, pady=1)
        
        self.button_glycemie = tk.Button(self.accueil_frame, text="Glycémie", command=self.open_GlycemieFrame, font=("Helvetica", 18, "bold"), background="#00CBE9")
        self.button_glycemie.grid(row=2, column=2, pady=1)

        # Configurer les poids des lignes et des colonnes pour que le contenu soit centré
        self.accueil_frame.grid_rowconfigure(0, weight=1)
        self.accueil_frame.grid_rowconfigure(2, weight=1)
        self.accueil_frame.grid_columnconfigure(0, weight=1)
        self.accueil_frame.grid_columnconfigure(2, weight=1)


    def open_PressionFrame(self):
        self.destroy()
        pression_frame = Pression()

    def open_GlycemieFrame(self):
        self.destroy()
        glycemie_frame = Glycemie()

    def close_Accueil(self):
        self.destroy()


# Classe Pression
class Pression(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Pression Artérielle")
        self.geometry("500x334")
        self.configure(bg='#03F2F1')

        self.background_image = tk.PhotoImage(file="pression.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Création d'une frame pour contenir les widgets avec fond blanc
        self.frame = tk.Frame(self, bg='white')
        self.frame.pack(padx=50, pady=50, fill='both', expand=True)

        # Création des widgets dans la frame
        self.label_diastolique = tk.Label(self.frame, text="Pression Diastolique:", font=("Helvetica", 14), bg='white')
        self.label_diastolique.pack()

        self.entry_diastolique = tk.Entry(self.frame, font=("Helvetica", 14))
        self.entry_diastolique.pack()

        self.label_systolique = tk.Label(self.frame, text="Pression Systolique:", font=("Helvetica", 14), bg='white')
        self.label_systolique.pack()

        self.entry_systolique = tk.Entry(self.frame, font=("Helvetica", 14))
        self.entry_systolique.pack()

        self.button_calculer = tk.Button(self.frame, text="Calculer", font=("Helvetica", 14), command=self.calculer, bg='#ADD8E6')
        self.button_calculer.pack()

        self.button_retour = tk.Button(self.frame, text="Retour", font=("Helvetica", 14), command=self.close_pressionFrame, bg='#ADD8E6')
        self.button_retour.pack()

        self.summary_label = tk.Label(self.frame, text="", font=("Helvetica", 14), bg='white')
        self.summary_label.pack(pady=10)

    def close_pressionFrame(self):
        self.destroy()
        accueil = PageAccueil()




    def calculer(self):
        diastolique = float(self.entry_diastolique.get())
        systolique = float(self.entry_systolique.get())
        pression_choice = 'choix_pression'  # Votre choix de pression floue ici
        pression_etat = etatPression(diastolique, systolique, pression_choice)
        if pression_etat is not None:
            self.summary_label.config(text=f"État de la pression: {pression_etat}")
        else:
             self.summary_label.config(text="Calcul Impossible")

# Classe Glycemie
class Glycemie(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Glycémie")
        self.geometry("500x334")
        self.configure(bg='#03F2F1')

        self.background_image = tk.PhotoImage(file="glycemie.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Création d'une frame pour contenir les widgets avec fond blanc
        self.frame = tk.Frame(self, bg='white')
        self.frame.pack(padx=50, pady=50, fill='both', expand=True)

        # Création des widgets dans la frame
        self.label_avant_repas = tk.Label(self.frame, text="Glycémie Avant Repas:", font=("Helvetica", 14), bg='white')
        self.label_avant_repas.pack()

        self.entry_avant_repas = tk.Entry(self.frame, font=("Helvetica", 14))
        self.entry_avant_repas.pack()

        self.label_apres_repas = tk.Label(self.frame, text="Glycémie Après Repas:", font=("Helvetica", 14), bg='white')
        self.label_apres_repas.pack()

        self.entry_apres_repas = tk.Entry(self.frame, font=("Helvetica", 14))
        self.entry_apres_repas.pack()

        self.button_calculer = tk.Button(self.frame, text="Calculer", font=("Helvetica", 14), command=self.calculer, bg='#ADD8E6')
        self.button_calculer.pack()

        self.button_retour = tk.Button(self.frame, text="Retour", font=("Helvetica", 14), command=self.close_glycemieFrame, bg='#ADD8E6')
        self.button_retour.pack()

        self.summary_label = tk.Label(self.frame, text="", font=("Helvetica", 14), bg='white')
        self.summary_label.pack(pady=10)

    def close_glycemieFrame(self):
        self.destroy()
        accueil = PageAccueil()
        

    



    def calculer(self):
        avant_repas = float(self.entry_avant_repas.get())
        apres_repas = float(self.entry_apres_repas.get())
        glycemie_choice = 'choix_glycemie'  # Votre choix de glycémie floue ici
        glycemie_etat = etatGlycemie(avant_repas, apres_repas, glycemie_choice)
        if glycemie_etat is not None:
            self.summary_label.config(text=f"État de la glycémie: {glycemie_etat}")
        else:
            self.summary_label.config(text="Calcul Impossible")

if __name__ == '__main__':
    app = PageAccueil()
    app.mainloop()

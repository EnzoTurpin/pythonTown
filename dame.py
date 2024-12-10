from humain import Humain

# Classe Dame héritant de Humain
class Dame(Humain):
    def __init__(self, nom, couleur_robe):
        super().__init__(nom, "lait")
        self.couleur_robe = couleur_robe
        self.libre = True

    def enlever(self):
        self.libre = False
        self.parle("Aaaah ! Au secours !")

    def liberer(self):
        self.libre = True
        self.parle("Merci beaucoup, vous êtes mon héros !")

    def changer_robe(self, nouvelle_couleur):
        self.couleur_robe = nouvelle_couleur
        self.parle(f"Regardez ma nouvelle robe {self.couleur_robe} !")

    def presentation(self):
        super().se_presenter()
        self.parle(f"J'adore ma robe de couleur {self.couleur_robe}.")

    def quel_est_ton_nom(self):
        return f"Miss {super().quel_est_ton_nom()}"

    def manger(self):
        self.parle("Je mange délicatement, comme une dame.")

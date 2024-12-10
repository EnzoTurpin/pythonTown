from cowboy import Cowboy

# Classe Shérif héritant de Cowboy
class Sherif(Cowboy):
    def __init__(self, nom):
        super().__init__(nom, "honnête")
        self.brigands_coffres = 0

    def coffrer(self, brigand):
        self.parle("Au nom de la loi, je vous arrête !")
        brigand.emprisonner(self)
        self.brigands_coffres += 1

    def rechercher(self, brigand):
        print(f"OYEZ OYEZ BRAVE GENS !! {brigand.recompense} $ à qui arrêtera {brigand.quel_est_ton_nom()} mort ou vif !")

    def presentation(self):
        super().presentation()
        self.parle(f"J'ai coffré {self.brigands_coffres} brigands.")

    def quel_est_ton_nom(self):
        return f"Shérif {super().quel_est_ton_nom()}"

    def manger(self):
        self.parle("Je mange comme un shérif, avec dignité.")

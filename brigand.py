from humain import Humain

# Classe Brigand héritant de Humain
class Brigand(Humain):
    def __init__(self, nom, look="méchant", recompense=100):
        super().__init__(nom, "tord-boyaux")
        self.look = look
        self.recompense = recompense
        self.dames_enlevees = 0
        self.en_prison = False

    def kidnapper(self, dame):
        self.parle(f"Ah ah ! {dame.quel_est_ton_nom()}, tu es mienne désormais !")
        dame.enlever()

    def presentation(self):
        super().se_presenter()
        self.parle(f"J'ai l'air {self.look} et j'ai déjà kidnappé {self.dames_enlevees} dames !")
        self.parle(f"Ma tête est mise à prix {self.recompense} $ !")

    def quel_est_ton_nom(self):
        return f"{super().quel_est_ton_nom()} le {self.look}"

    def emprisonner(self, cowboy):
        self.parle(f"Damned, je suis fait ! {cowboy.quel_est_ton_nom()}, tu m’as eu !")
        self.en_prison = True

    def manger(self):
        self.parle("Je mange comme un brigand, salement et bruyamment.")

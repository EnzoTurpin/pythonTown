from humain import Humain

# Classe Cowboy héritant de Humain
class Cowboy(Humain):
    def __init__(self, nom, adjectif="vaillant"):
        super().__init__(nom, "whisky")
        self.adjectif = adjectif
        self.popularite = 0

    def tirer(self, brigand):
        print(f"Le {self.adjectif} {self.quel_est_ton_nom()} tire sur {brigand.quel_est_ton_nom()}. PAN !")
        self.parle("Prend ça, rascal !")

    def liberer(self, dame):
        self.parle(f"Ne vous inquiétez pas, {dame.quel_est_ton_nom()}, vous êtes libre maintenant !")
        dame.liberer()
        self.popularite += 1

    def presentation(self):
        super().se_presenter()
        self.parle(f"On dit de moi que je suis {self.adjectif} et ma popularité est de {self.popularite}.")

    def manger(self):
        self.parle("Je mange vite mais proprement, comme un cowboy respectable.")

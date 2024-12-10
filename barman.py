from humain import Humain

# Classe Barman héritant de Humain
class Barman(Humain):
    def __init__(self, nom, nom_bar=None):
        super().__init__(nom, "Vin")
        self.nom_bar = nom_bar if nom_bar else f"Chez {nom}"

    def presentation(self):
        super().se_presenter()
        self.parle(f"Bienvenue dans mon bar {self.nom_bar}.")

    def parle(self, texte):
        super().parle(f"{texte} Coco.")

    def servir(self, humain):
        self.parle(f"Voici votre verre de {humain.quelle_est_ta_boisson_favorite()}.")

    def manger(self):
        self.parle("Je grignote tout en servant mes clients.")

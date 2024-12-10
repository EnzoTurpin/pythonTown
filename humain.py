from abc import ABC, abstractmethod

# Classe de base Humain
class Humain(ABC):
    def __init__(self, nom, boisson_favorite="eau"):
        self.__nom = nom
        self.__boisson_favorite = boisson_favorite

    def parle(self, texte):
        print(f"{self.__nom} - {texte}")

    def se_presenter(self):
        self.parle(f"Bonjour, je suis {self.__nom} et j'aime le {self.__boisson_favorite}.")

    def boire(self):
        self.parle(f"Ah ! un bon verre de {self.__boisson_favorite} ! GLOUPS !")

    def quel_est_ton_nom(self):
        return self.__nom

    def quelle_est_ta_boisson_favorite(self):
        return self.__boisson_favorite

    @abstractmethod
    def manger(self):
        pass

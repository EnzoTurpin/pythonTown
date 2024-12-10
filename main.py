from cowboy import Cowboy
from dame import Dame
from brigand import Brigand
from barman import Barman
from sherif import Sherif

if __name__ == "__main__":
    john = Cowboy("John")
    jane = Dame("Jane", "rouge")
    bob = Brigand("Bob")
    barney = Barman("Barney")
    sheriff = Sherif("Wyatt")

    john.presentation()
    jane.presentation()
    bob.presentation()
    barney.presentation()
    sheriff.presentation()

    bob.kidnapper(jane)
    john.liberer(jane)
    sheriff.coffrer(bob)
    barney.servir(john)
    sheriff.rechercher(bob)

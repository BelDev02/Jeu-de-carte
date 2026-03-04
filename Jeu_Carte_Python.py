import random

class Carte:
    """Représente une carte avec une couleur et une valeur"""
    order_valeur = ["7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def __repr__(self):
        return f"Carte({self.couleur}, {self.valeur})"

    def __eq__(self, autre_carte):
        return self.valeur == autre_carte.valeur and self.couleur == autre_carte.couleur

    def __lt__(self, autre_carte):
        return self.order_valeur.index(self.valeur) < self.order_valeur.index(autre_carte.valeur)


class Desc:
    """Représente un jeu de cartes (deck)"""

    def __init__(self):
        valeurs = ["7", "8", "9", "10", "J", "Q", "K", "A"]
        couleurs = ["Coeur", "Pique", "Carreau", "Trefle"]
        self.cartes = [Carte(c, v) for c in couleurs for v in valeurs]
        random.shuffle(self.cartes)

    def __len__(self):
        return len(self.cartes)

    def __getitem__(self, position):
        return self.cartes[position]

    def __setitem__(self, position, valeur):
        if isinstance(valeur, Carte):
            self.cartes[position] = valeur
        else:
            raise TypeError("Vous faites une mauvaise assignation, ce n'est pas une Carte.")

    def trie(self):
        """Retourne le jeu trié par valeur"""
        return sorted(self.cartes)


# --- Programme principal ---

mon_jeu = Desc()

# Affichage des cartes du jeu
for carte in mon_jeu:
    print(carte)

print(f"\nNotre jeu comporte {len(mon_jeu)} cartes")
print(f"La première carte du jeu est: {mon_jeu[0]}")
print(f"La dernière carte du jeu est: {mon_jeu[-1]}")

# Affichage des 7 premières cartes
print("\nLes 7 premières cartes du jeu:")
for position in range(7):
    print(mon_jeu[position])

# Affichage du jeu trié
print("\nJeu trié par valeur:")
print(mon_jeu.trie())

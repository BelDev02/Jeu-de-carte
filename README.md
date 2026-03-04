# 🎴 Jeu de Cartes en Python

## 📌 Description

Ce projet implémente un jeu de cartes standard de 32 cartes (de 7 à As) avec les 4 couleurs : Coeur, Pique, Carreau et Trèfle.  

Le programme permet de créer un jeu, de mélanger les cartes, d’accéder aux cartes individuellement, de modifier des cartes et de trier le jeu par valeur.

Cette version inclut une structure orientée objet avec les classes `Carte` et `Desc` pour gérer les cartes et le jeu.

---

## 📝 Sujet du projet

### Instructions de base :

- Créer une classe `Carte` représentant une carte avec une couleur et une valeur
- Créer une classe `Desc` représentant le jeu de cartes
- Initialiser le jeu avec toutes les combinaisons possibles de couleurs et valeurs
- Mélanger le jeu à l’instanciation
- Permettre l’accès aux cartes par index
- Autoriser la modification d’une carte via un index (avec vérification du type)
- Afficher le jeu trié par valeur

### Extensions ajoutées :

- Tri automatique des cartes
- Affichage détaillé du jeu complet et de certaines cartes
- Support de la notation spéciale Python (`__len__`, `__getitem__`, `__setitem__`) pour manipuler le jeu comme une liste

---

## 🎮 Fonctionnalités implémentées

✔ Création d’une carte avec couleur et valeur  
✔ Création d’un jeu de cartes complet  
✔ Mélange automatique du jeu  
✔ Accès aux cartes via un index  
✔ Modification sécurisée des cartes  
✔ Tri du jeu par valeur  
✔ Affichage du jeu complet et des cartes sélectionnées  
✔ Code structuré avec classes et méthodes  

---

## 🧠 Structure du jeu

| Classe     | Description |
|------------|-------------|
| `Carte`    | Représente une carte unique avec couleur et valeur |
| `Desc`     | Conteneur pour toutes les cartes, avec mélange, accès, modification et tri |

---
## 🛠️ Technologies utilisées

- **Python 3**  
- Module standard `random` (pour mélanger le jeu)  
- Classes et objets pour la programmation orientée objet  
- Méthodes spéciales Python (`__len__`, `__getitem__`, `__setitem__`)  
- Boucles (`for`) et conditions (`if`)  
- Tri de listes avec `sorted()`  

## 🏆 Utilisation du jeu

```python
from jeu_cartes import Desc, Carte

# Création et mélange du jeu
mon_jeu = Desc()

# Affichage de la première et dernière carte
print(mon_jeu[0])
print(mon_jeu[-1])

# Affichage des 7 premières cartes
for i in range(7):
    print(mon_jeu[i])

# Trier le jeu et afficher
jeu_trie = mon_jeu.trie()
print(jeu_trie)
